import {
  GetSymbolArray,
  AddSymbolListener
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { getIndex } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { Fieldset } from 'primereact/fieldset';
import { useEffect, useState } from 'react';
import '../../Styles/memory.css';
import { ByteToHex, SetSliderValueLowerValueSymbolType } from './MemoryLogics';
import { component_id, fixedRegionColor } from '../MainView/TrustZoneMainView';
import {
  boxWidth,
  GetBoxTopHeight,
  GetBoxWithText,
  GetMemoryInBytes,
  GetTop0x0Text,
  sliderPaddingRight,
  sliderWidth,
  TOTAL_HEIGHT
} from './Memory';
import {
  UpdateSymbolValue,
  GetSymbolValue
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { ConfigSymbolEvent } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { GetBSOrASDiv, GetBootRegion } from './FlashUtils';

let MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE = 'IDAU_BNSC_SIZE';
let BASE_GRANULARITY = 'IDAU_ANSC_GRANULARITY';
let MEMORY_BOOT_SECURE_SIZE = 'IDAU_BS_SIZE';
let MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE = 'IDAU_ANSC_SIZE';
let MEMORY_APPLICATION_NON_SECURE_SIZE = 'IDAU_ANS_SIZE';
let MEMORY_APPLICATION_SECURE_SIZE = 'IDAU_AS_SIZE';

const FlashMemory = () => {
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

  useEffect(() => {
    addSymbolListeneres();
  }, []);

  let baseGranularity = GetSymbolValue(component_id, BASE_GRANULARITY);

  let deviceFlashTotalSize = GetSymbolValue(component_id, 'DEVICE_TOTAL_CODE_SIZE');

  let bootProtSize = GetSymbolValue(component_id, 'DEVICE_BOOTPROT_SIZE');
  let applicationtotalSize = GetSymbolValue(component_id, 'DEVICE_FLASH_SIZE');

  function addSymbolListeneres() {
    addListener(MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE);
    addListener(MEMORY_APPLICATION_NON_SECURE_SIZE);
    addListener(MEMORY_APPLICATION_SECURE_SIZE);
    addListener(MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE);
    addListener(MEMORY_BOOT_SECURE_SIZE);
  }

  const symbolChanged = (symbol: ConfigSymbolEvent) => {
    switch (symbol.symbolID) {
      case MEMORY_APPLICATION_SECURE_SIZE:
        setApplicationSecureSizeIndex(getIndex(symbol.value, applicationSecureArray));
        break;
      case MEMORY_BOOT_SECURE_SIZE:
        setBootSecureSizeIndex(getIndex(symbol.value, bootSecureArray));
        break;
      case MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE:
        setSlider1Value(getIndex(symbol.value, bootNonSecureCallableArray));
        break;
      case MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE:
        setSlider3Value(getIndex(symbol.value, applicationNonSecureCallableArray));
        break;
      case MEMORY_APPLICATION_NON_SECURE_SIZE:
        setSlider2Value(getIndex(symbol.value, applicationNonSecureArray));
        break;
    }
  };

  function addListener(symbolId: string) {
    AddSymbolListener(symbolId);
    globalSymbolSStateData.set(symbolId, {
      symbolChanged: symbolChanged
    });
  }

  // boot calculations////

  let bootSecureArray = GetSymbolArray(component_id, MEMORY_BOOT_SECURE_SIZE);

  let bootNonSecureCallableArray = GetSymbolArray(
    component_id,
    MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE
  );
  let bootNonSecureCallableIndex = getIndex(
    GetSymbolValue(component_id, MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE),
    bootNonSecureCallableArray
  );

  // boot end/////////////////

  // applciation start////////////////////////

  let applicationNonSecureArray = GetSymbolArray(component_id, MEMORY_APPLICATION_NON_SECURE_SIZE);
  let applicationNonSecureIndex = getIndex(
    GetSymbolValue(component_id, MEMORY_APPLICATION_NON_SECURE_SIZE),
    applicationNonSecureArray
  );

  let applicationSecureArray = GetSymbolArray(component_id, MEMORY_APPLICATION_SECURE_SIZE);
  let applicationNonSecureCallableArray = GetSymbolArray(
    component_id,
    MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE
  );
  let applicationNonSecureCallableIndex = getIndex(
    GetSymbolValue(component_id, MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE),
    applicationNonSecureCallableArray
  );

  /////////// application end//////////

  let fixedRegion = Number(GetSymbolValue(component_id, 'SEC_START_ADDRESS'));

  let topStartAddress = GetSymbolValue(component_id, 'BOOTPROT_SEC_START_ADDRESS');

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
    let dif = sliderMax - sliderRange;
    let newValue = Math.round((15 * dif) / 100);
    if (newValue > 5) {
      sliderMax = 5;
    } else {
      sliderMax = newValue;
    }
    return sliderMax;
  }

  let flashSizeLabel = 'FLASH ( ' + GetMemoryInBytes(deviceFlashTotalSize) + ' )';

  // Slider 1
  slider1Min = 0;
  slider1Max = bootSecureArray.length - 1;
  nSlider1RestricRange = bootNonSecureCallableArray.length - 1;
  if (slider1Max > nSlider1RestricRange) {
    slider1Max = GetNewMaxValue(slider1Max, nSlider1RestricRange);
  }

  const [slider1Value, setSlider1Value] = useState<number | number>(
    SetSliderValueLowerValueSymbolType(bootNonSecureCallableIndex, slider1Max)
  );
  const [bootSecureSizeIndex, setBootSecureSizeIndex] = useState<number | number>(
    getIndex(GetSymbolValue(component_id, MEMORY_BOOT_SECURE_SIZE), bootSecureArray)
  );
  /////

  // Slider 2
  slider2Min = 0;
  slider2Max = applicationNonSecureArray.length - 1;
  nSlider2RestricRange = slider2Max;
  const [slider2Value, setSlider2Value] = useState<number | number>(
    SetSliderValueLowerValueSymbolType(applicationNonSecureIndex, slider2Max)
  );
  /////

  // Slider 3
  slider3Min = 0;
  slider3Max = applicationSecureArray.length - 1;
  nSlider3RestricRange = applicationNonSecureCallableArray.length - 1;
  if (slider3Max > nSlider3RestricRange) {
    slider3Max = GetNewMaxValue(slider3Max, nSlider3RestricRange);
  }
  const [slider3Value, setSlider3Value] = useState<number | number>(
    SetSliderValueLowerValueSymbolType(applicationNonSecureCallableIndex, slider3Max)
  );
  const [applicationSecureSizeIndex, setApplicationSecureSizeIndex] = useState<number | number>(
    getIndex(GetSymbolValue(component_id, MEMORY_APPLICATION_SECURE_SIZE), applicationSecureArray)
  );

  /////

  UpdateSliderAndBoxHeight(slider2Value);

  function updateSlider1Value(value: any) {
    if (value > nSlider1RestricRange) {
      value = nSlider1RestricRange;
    }
    setSlider1Value(value);
    UpdateSymbolValue(
      component_id,
      MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE,
      bootNonSecureCallableArray[value]
    );
  }
  function updateSlider2Value(value: any) {
    if (value > nSlider2RestricRange) {
      value = nSlider2RestricRange;
    }
    UpdateSliderAndBoxHeight(value);
    setSlider2Value(value);
    UpdateSymbolValue(
      component_id,
      MEMORY_APPLICATION_NON_SECURE_SIZE,
      applicationNonSecureArray[value]
    );
  }
  function updateSlider3Value(value: any) {
    if (value > nSlider3RestricRange) {
      value = nSlider3RestricRange;
    }
    setSlider3Value(value);
    UpdateSymbolValue(
      component_id,
      MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE,
      applicationNonSecureCallableArray[value]
    );
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

    nBytes = bootSecureSizeIndex * baseGranularity;
    nTotal = nTotal + nBytes;
    box1Text = nBytes.toLocaleString() + ' Bytes';
    box1HexText = ByteToHex(nTotal);

    nBytes = slider1Value * baseGranularity;
    nTotal = nTotal + nBytes;
    box2Text = nBytes.toLocaleString() + ' Bytes';
    box2HexText = ByteToHex(nTotal);

    nBytes = 0;
    nTotal = 0;

    nBytes = fixedRegion;
    nTotal = nTotal + nBytes;
    box3HexText = ByteToHex(nTotal);

    nBytes = applicationSecureSizeIndex * baseGranularity;
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
              {GetBoxWithText(
                'flex flex-row',
                'Reserved Section',
                fixedRegionColor,
                boxTopFixedHeight,
                boxTopFixedRegionHexText,
                true
              )}
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
              {GetBoxWithText(
                'flex flex-row',
                'Other Regions/Reserved',
                fixedRegionColor,
                box3Height,
                box3HexText,
                true
              )}
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
