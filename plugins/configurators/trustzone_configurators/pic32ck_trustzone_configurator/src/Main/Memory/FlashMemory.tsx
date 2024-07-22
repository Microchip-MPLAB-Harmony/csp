import { Fieldset } from 'primereact/fieldset';
import { useContext, useEffect } from 'react';
import { ByteToHex } from './MemoryLogics';
import { fixedRegionColor } from '../MainView/TrustZoneMainView';
import {
  boxWidth,
  GetBoxTopHeight,
  GetMemoryInBytes,
  GetTop0x0Text,
  sliderPaddingRight,
  sliderWidth,
  TOTAL_HEIGHT
} from './Memory';
import {
  info,
  PluginConfigContext,
  useHexSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import GetBoxWithText from './GetBoxWithText';
import { GetBootRegion, GetBSOrASDiv } from './FlashUtils';

let previousSlider1Value = -1;
let previousSlider2Value = -1;
let previousSlider3Value = -1;
const FlashMemory = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  let topLabelPosition =
    sliderWidth + sliderPaddingRight + sliderPaddingRight + sliderPaddingRight + 10 + boxWidth;
  let fixedRegionPadding =
    sliderPaddingRight + sliderPaddingRight + sliderWidth + sliderWidth + sliderWidth;
  let slider1Height = 0;
  let slider2Height = 0;
  let slider3Height = 0;
  let nonSecureBoxPaddingLeft = sliderPaddingRight + sliderWidth;
  let bootPadding = sliderPaddingRight + sliderWidth + sliderWidth;
  let slider1Min: any, slider1Max: any, nSlider1RestricRange: any;
  let slider2Min: any, slider2Max: any, nSlider2RestricRange: any;
  let slider3Min: any, slider3Max: any, nSlider3RestricRange: any;
  let box1Text: any, box1HexText: any;
  let box2Text: any, box2HexText: any;
  let box3HexText: any;
  let box4Text: any, box4HexText: any;
  let box5Text: any, box5HexText: any;
  let box6Text: any, box6HexText: any;
  let boxTopFixedRegionHexText: any;
  let box3Height;
  useEffect(() => {}, []);
  const baseGranularitySymbol = useIntegerSymbol({
    componentId: componentId,
    symbolId: 'IDAU_ANSC_GRANULARITY'
  });
  let baseGranularity = baseGranularitySymbol.value;
  const deviceFlashTotalSizeSymbol = useIntegerSymbol({
    componentId: componentId,
    symbolId: 'DEVICE_TOTAL_CODE_SIZE'
  });
  const ansGranularity = useIntegerSymbol({
    componentId: componentId,
    symbolId: 'IDAU_ANS_GRANULARITY'
  });
  let deviceFlashTotalSize = deviceFlashTotalSizeSymbol.value;

  const bootProtSizeSymbol = useIntegerSymbol({
    componentId: componentId,
    symbolId: 'DEVICE_BOOTPROT_SIZE'
  });
  let bootProtSize = bootProtSizeSymbol.value;
  const applicationTotalSizeSymbol = useIntegerSymbol({
    componentId: componentId,
    symbolId: 'DEVICE_FLASH_SIZE'
  });
  let applicationtotalSize = applicationTotalSizeSymbol.value;

  const fixedRegionSymbol = useHexSymbol({
    componentId: componentId,
    symbolId: 'SEC_START_ADDRESS'
  });
  const topStartAddressSymbol = useHexSymbol({
    componentId: componentId,
    symbolId: 'BOOTPROT_SEC_START_ADDRESS'
  });

  const memoryApplicationSecureSizeSymbol = useKeyValueSetSymbol({
    componentId: componentId,
    symbolId: 'IDAU_AS_SIZE'
  });
  const memoryApplicationNonSecureCallableSizeSymbol = useKeyValueSetSymbol({
    componentId: componentId,
    symbolId: 'IDAU_ANSC_SIZE'
  });
  const memoryApplicationNonSecureSizeSymbol = useKeyValueSetSymbol({
    componentId: componentId,
    symbolId: 'IDAU_ANS_SIZE'
  });
  const memoryBootNonSecureCallableSizeSymbol = useKeyValueSetSymbol({
    componentId: componentId,
    symbolId: 'IDAU_BNSC_SIZE'
  });
  const memoryBootSecureSizeSymbol = useKeyValueSetSymbol({
    componentId: componentId,
    symbolId: 'IDAU_BS_SIZE'
  });

  /////////// application end//////////
  let fixedRegion = Number(fixedRegionSymbol.value);
  let topStartAddress = topStartAddressSymbol.value;
  let tempTotal = bootProtSize + applicationtotalSize;
  let boxTopFixedHeight = (10 * TOTAL_HEIGHT) / 100;
  slider1Height = (GetSizePercentage(bootProtSize, tempTotal) * TOTAL_HEIGHT) / 100;
  box3Height = (10 * TOTAL_HEIGHT) / 100;
  slider2Height = TOTAL_HEIGHT - slider1Height - box3Height - boxTopFixedHeight;
  function GetSizePercentage(value: any, total: any) {
    let percentage = (value / total) * 100;
    if (percentage < 20) {
      return 20;
    }
    return percentage;
  }
  function GetNewMaxValue(sliderMax: any, sliderRange: any) {
    if (sliderRange < 3) {
      sliderMax = 3;
    }
    return sliderMax;
  }
  let flashSizeLabel = 'FLASH ( ' + GetMemoryInBytes(deviceFlashTotalSize) + ' )';
  // Slider 1
  slider1Min = 0;
  slider1Max = memoryBootSecureSizeSymbol.options.length - 1;
  nSlider1RestricRange = memoryBootNonSecureCallableSizeSymbol.options.length - 1;
  if (slider1Max > nSlider1RestricRange) {
    slider1Max = GetNewMaxValue(slider1Max, nSlider1RestricRange);
  }
  const slider1Value = memoryBootNonSecureCallableSizeSymbol.value;
  /////
  // Slider 3
  slider3Min = 0;
  slider3Max = memoryApplicationSecureSizeSymbol.options.length - 1;
  nSlider3RestricRange = memoryApplicationNonSecureCallableSizeSymbol.options.length - 1;
  if (slider3Max > nSlider3RestricRange) {
    slider3Max = GetNewMaxValue(slider3Max, nSlider3RestricRange);
  }
  const slider3Value = memoryApplicationNonSecureCallableSizeSymbol.value;
  // Slider 2
  slider2Min = 0;
  slider2Max = applicationTotalSizeSymbol.value / ansGranularity.value;
  nSlider2RestricRange = slider2Max - slider3Value;
  const slider2Value = memoryApplicationNonSecureSizeSymbol.value;
  /////
  UpdateSliderAndBoxHeight(slider2Value);
  function updateSlider1Value(value: any) {
    if (value > nSlider1RestricRange) {
      value = nSlider1RestricRange;
    }
    if (previousSlider1Value !== value) {
      memoryBootNonSecureCallableSizeSymbol.writeValue(
        memoryBootNonSecureCallableSizeSymbol.options[value]
      );
      previousSlider1Value = value;
    }
  }
  function updateSlider2Value(value: any) {
    if (value > nSlider2RestricRange) {
      value = nSlider2RestricRange;
    }

    UpdateSliderAndBoxHeight(value);
    if (previousSlider2Value !== value) {
      memoryApplicationNonSecureSizeSymbol.writeValue(
        memoryApplicationNonSecureSizeSymbol.options[value]
      );
      previousSlider2Value = value;
    }
  }
  function updateSlider3Value(value: any) {
    if (value > nSlider3RestricRange) {
      value = nSlider3RestricRange;
    }
    if (previousSlider3Value !== value) {
      memoryApplicationNonSecureCallableSizeSymbol.writeValue(
        memoryApplicationNonSecureCallableSizeSymbol.options[value]
      );
      previousSlider3Value = value;
    }
  }
  function UpdateSliderAndBoxHeight(slider2Value: any) {
    slider3Height = GetBoxTopHeight(slider2Value, slider2Max, slider2Height);
    UpdateFlashMemoryLabelValues();
  }
  function UpdateFlashMemoryLabelValues() {
    let nBytes = 0;
    let nTotal = 0;
    nBytes = Number(topStartAddress);
    nTotal = nTotal + nBytes;
    boxTopFixedRegionHexText = ByteToHex(nBytes);
    nBytes = memoryBootSecureSizeSymbol.value * baseGranularity;
    nTotal = nTotal + nBytes;
    box1Text = nBytes.toLocaleString() + ' Bytes';
    box1HexText = ByteToHex(nTotal);
    nBytes = memoryBootNonSecureCallableSizeSymbol.value * baseGranularity;
    nTotal = nTotal + nBytes;
    box2Text = nBytes.toLocaleString() + ' Bytes';
    box2HexText = ByteToHex(nTotal);
    nBytes = 0;
    nTotal = 0;
    nBytes = fixedRegion;
    nTotal = nTotal + nBytes;
    box3HexText = ByteToHex(nTotal);
    nBytes = memoryApplicationSecureSizeSymbol.value * baseGranularity;
    nTotal = nTotal + nBytes;
    box4Text = nBytes.toLocaleString() + ' Bytes';
    box4HexText = ByteToHex(nTotal);
    nBytes = slider3Value * baseGranularity;
    nTotal = nTotal + nBytes;
    box5Text = nBytes.toLocaleString() + ' Bytes';
    box5HexText = ByteToHex(nTotal);
    nBytes = slider2Value * baseGranularity;
    nTotal = nTotal + nBytes;
    box6Text = nBytes.toLocaleString() + ' Bytes';
    box6HexText = ByteToHex(nTotal);
  }
  return (
    <div>
      <div className='flex'>
        <Fieldset
          className=' flash m-2'
          legend={flashSizeLabel}>
          <div className='flex flex-column'>
            {GetTop0x0Text(topLabelPosition)}
            <div
              className='flex border-top-2'
              style={{ paddingLeft: fixedRegionPadding + 'px' }}>
              <GetBoxWithText
                classCustom={'flex flex-row'}
                displayText={'Reserved Section'}
                color={fixedRegionColor}
                boxHeight={boxTopFixedHeight}
                hexDisplayText={boxTopFixedRegionHexText}
                textDisplayStatus={true}
              />
            </div>
            <div>
              {GetBootRegion(
                slider1Value,
                slider1Min,
                slider1Max,
                slider1Height,
                updateSlider1Value,
                box1Text,
                box1HexText,
                box2Text,
                box2HexText,
                bootPadding
              )}
            </div>
            <div style={{ paddingLeft: fixedRegionPadding + 'px' }}>
              <GetBoxWithText
                classCustom={'flex flex-row'}
                displayText={'Other Regions/Reserved'}
                color={fixedRegionColor}
                boxHeight={box3Height}
                hexDisplayText={box3HexText}
                textDisplayStatus={true}
              />
            </div>
            <div className=''></div>
            <div>
              <div className='flex flex-column border-y-2'>
                <div>
                  {GetBSOrASDiv(
                    'flex flex-row',
                    '',
                    'ANS',
                    'AS',
                    'ANSC',
                    slider2Value,
                    slider2Min,
                    slider2Max,
                    slider2Height,
                    updateSlider2Value,
                    slider3Value,
                    slider3Min,
                    slider3Max,
                    slider3Height,
                    updateSlider3Value,
                    box4Text,
                    box4HexText,
                    box5Text,
                    box5HexText,
                    box6Text,
                    box6HexText,
                    true,
                    nonSecureBoxPaddingLeft
                  )}
                </div>
              </div>
            </div>
          </div>
        </Fieldset>
      </div>
    </div>
  );
};
export default FlashMemory;
