import {
  GetSymbolArray,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { getIndex } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import { Fieldset } from 'primereact/fieldset';
import { useState } from 'react';
import '../../Styles/memory.css';
import { ByteToHex, SetSliderValueLowerValueSymbolType } from './MemoryLogics';
import {
  component_id,
  nonSecureCallableColor,
  nonSecureColor,
  secureColor,
} from '../MainView/TrustZoneMainView';
import {
  boxWidth,
  GetBoxBottomHeight,
  GetBoxTopHeight,
  GetBoxWithText,
  GetMemoryInBytes,
  GetSlider,
  GetTop0x0Text,
  sliderPaddingRight,
  sliderWidth,
  TOTAL_HEIGHT,
} from './Memory';
import {
  GetValidSilderSymbolValue,
  SetMinMaxSliderCallableSlider,
  SetSliderValueUpperValueSymbolType,
} from './MemoryLogics';
import { error } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';
import { UpdateSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

let MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE = 'IDAU_BNSC_SIZE';
let MEMORY_BOOT_SECURE_SIZE = 'IDAU_BS_SIZE';
let MEMORY_BOOT_PROTECTION_SIZE = 'IDAU_BOOTPROT_SIZE';
let MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE = 'IDAU_ANSC_SIZE';
let MEMORY_APPLICATION_SECURE_SIZE = 'IDAU_AS_SIZE';

let BOOT_NON_SECURE_GRANULARITY = 'IDAU_BNSC_GRANULARITY';
let BOOT_SECURE_GRANULARITY = 'IDAU_BS_GRANULARITY';
let BOOT_PROTECTION_GRANULARITY = 'IDAU_BOOTPROT_GRANULARITY';
let APPLICATION_NON_SECURE_GRANULARITY = 'IDAU_ANSC_GRANULARITY';
let APPLICATION_SECURE_GRANULARITY = 'IDAU_AS_GRANULARITY';

const FlashMemory = () => {
  let topLabelPosition =
    sliderWidth +
    sliderPaddingRight +
    sliderPaddingRight +
    sliderPaddingRight +
    sliderPaddingRight +
    10 +
    boxWidth;
  let nonSecureBoxPaddingLeft = sliderPaddingRight + sliderWidth;
  let slider1Height = TOTAL_HEIGHT;
  let slider2Height = 0;
  let slider3Height = 0;
  let slider4Height = 0;
  let slider5Height = 0;

  let slider1Min: any, slider1Max: any, nSlider1RestricRange: any;
  let slider2Min: any, slider2Max: any, nSlider2RestricRange: any;
  let slider3Min: any, slider3Max: any, nSlider3RestricRange: any;
  let slider4Min: any, slider4Max: any, nSlider4RestricRange: any;
  let slider5Min: any, slider5Max: any, nSlider5RestricRange: any;

  let box1Text: any, box1HexText: any;
  let box2Text: any, box2HexText: any;
  let box3Text: any, box3HexText: any;
  let box4Text: any, box4HexText: any;
  let box5Text: any, box5HexText: any;
  let box6Text: any, box6HexText: any;

  let nDeviceFlashTotalSize = GetSymbolValue(component_id, 'DEVICE_FLASH_SIZE');
  let flashSizeLabel =
    'FLASH ( ' + GetMemoryInBytes(nDeviceFlashTotalSize) + ' )';

  let nFlashBaseGranularity = GetSymbolValue(
    component_id,
    BOOT_PROTECTION_GRANULARITY
  );

  // Slider 1
  slider1Min = 0;
  slider1Max = nDeviceFlashTotalSize / nFlashBaseGranularity;
  nSlider1RestricRange = slider1Max;
  let bootProtectionSizeSymbolArray = GetSymbolArray(
    component_id,
    MEMORY_BOOT_PROTECTION_SIZE
  );
  let bootProtectionSymbolValue = getIndex(
    GetValidSilderSymbolValue(
      MEMORY_BOOT_PROTECTION_SIZE,
      slider1Max,
      nSlider1RestricRange
    ),
    bootProtectionSizeSymbolArray
  );
  const [slider1Value, setSlider1Value] = useState<number | number>(
    SetSliderValueUpperValueSymbolType(bootProtectionSymbolValue, slider1Max)
  );
  /////

  // Slider 2
  let nBootSecureGranularity = GetSymbolValue(
    component_id,
    BOOT_SECURE_GRANULARITY
  );
  let bootSecureSymbolArray = GetSymbolArray(
    component_id,
    MEMORY_BOOT_SECURE_SIZE
  );
  const [slider2Value, setSlider2Value] = useState<number | number>(
    UpdateSlider2Configuration(slider1Max, slider1Value)
  );
  function SetMinMax2(slider1Max: any, slider1Value: any) {
    slider2Min = 0;
    slider2Max = slider1Max - slider1Value;
    nSlider2RestricRange = slider2Max;
  }
  function UpdateSlider2Configuration(slider1Max: any, slider1Value: any) {
    SetMinMax2(slider1Max, slider1Value);
    let bootSecureSizeSymbolValue = getIndex(
      GetValidSilderSymbolValue(
        MEMORY_BOOT_SECURE_SIZE,
        slider2Max,
        nSlider2RestricRange
      ),
      bootSecureSymbolArray
    );

    return SetSliderValueUpperValueSymbolType(
      bootSecureSizeSymbolValue,
      slider2Max
    );
  }
  /////

  // Slider 3
  let nApplicationSecureGranularity = GetSymbolValue(
    component_id,
    APPLICATION_SECURE_GRANULARITY
  );
  let applicationSecureSymbolArray = GetSymbolArray(
    component_id,
    MEMORY_APPLICATION_SECURE_SIZE
  );
  const [slider3Value, setSlider3Value] = useState<number | number>(
    UpdateSlider3Configuration(slider1Value)
  );
  function SetMinMax3(slider1Value: any) {
    slider3Min = 0;
    slider3Max = slider1Value;
    nSlider3RestricRange = slider3Max;
  }
  function UpdateSlider3Configuration(slider1Value: any) {
    SetMinMax3(slider1Value);
    let applicationSecureSizeSymbolValue = getIndex(
      GetValidSilderSymbolValue(
        MEMORY_APPLICATION_SECURE_SIZE,
        slider3Max,
        nSlider3RestricRange
      ),
      applicationSecureSymbolArray
    );
    return SetSliderValueUpperValueSymbolType(
      applicationSecureSizeSymbolValue,
      slider3Max
    );
  }
  /////

  // Slider 4
  let nBootNonSecureCallableGranularity = GetSymbolValue(
    component_id,
    BOOT_NON_SECURE_GRANULARITY
  );
  let bootNonSecureCallableSymbolArray = GetSymbolArray(
    component_id,
    MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE
  );
  const [slider4Value, setSlider4Value] = useState<number | number>(
    UpdateSlider4Configuration(slider2Max, slider2Value)
  );
  function setMinMax_Slider4(min: any, max: any, restricValue: any) {
    slider4Min = min;
    slider4Max = max;
    nSlider4RestricRange = restricValue;
  }
  function UpdateSlider4Configuration(slider2Max: any, slider2Value: any) {
    SetMinMaxSliderCallableSlider(
      slider2Max - slider2Value,
      nBootNonSecureCallableGranularity,
      bootNonSecureCallableSymbolArray.length,
      setMinMax_Slider4
    );
    let bootNonSecureCallableSizeSymbolValue = getIndex(
      GetValidSilderSymbolValue(
        MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE,
        slider4Max,
        nSlider4RestricRange
      ),
      bootNonSecureCallableSymbolArray
    );
    return SetSliderValueLowerValueSymbolType(
      bootNonSecureCallableSizeSymbolValue,
      slider4Max
    );
  }
  /////

  // Slider 5
  let nApplicationNonSecureCallableGranularity = GetSymbolValue(
    component_id,
    APPLICATION_NON_SECURE_GRANULARITY
  );
  let applicationNonSecureCallableSymbolArray = GetSymbolArray(
    component_id,
    MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE
  );
  const [slider5Value, setSlider5Value] = useState<number | number>(
    UpdateSlider5Configuration(slider3Max, slider3Value)
  );
  function setMinMax_Slider5(min: any, max: any, restricValue: any) {
    slider5Min = min;
    slider5Max = max;
    nSlider5RestricRange = restricValue;
  }
  function UpdateSlider5Configuration(slider3Max: any, slider3Value: any) {
    SetMinMaxSliderCallableSlider(
      slider3Max - slider3Value,
      nApplicationNonSecureCallableGranularity,
      applicationNonSecureCallableSymbolArray.length,
      setMinMax_Slider5
    );
    let applicationNonSecureCallableSizeSymbolValue = getIndex(
      GetValidSilderSymbolValue(
        MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE,
        slider5Max,
        nSlider5RestricRange
      ),
      applicationNonSecureCallableSymbolArray
    );
    return SetSliderValueLowerValueSymbolType(
      applicationNonSecureCallableSizeSymbolValue,
      slider5Max
    );
  }
  /////

  UpdateSliderAndBoxHeight(slider1Value, slider2Value, slider3Value);

  function updateSlider1Value(value: any) {
    UpdateSliderAndBoxHeight(value, slider2Value, slider3Value);
    setSlider1Value(value);
    UpdateSymbolValue(
      component_id,
      MEMORY_BOOT_PROTECTION_SIZE,
      bootProtectionSizeSymbolArray[slider1Max - value]
    );
  }
  function updateSlider2Value(value: any) {
    UpdateSliderAndBoxHeight(slider1Value, value, slider3Value);
    setSlider2Value(value);
    UpdateSymbolValue(
      component_id,
      MEMORY_BOOT_SECURE_SIZE,
      bootSecureSymbolArray[slider2Max - value]
    );
    updateSlider4Value(UpdateSlider4Configuration(slider2Max, value));
  }
  function updateSlider3Value(value: any) {
    UpdateSliderAndBoxHeight(slider1Value, slider2Value, value);
    setSlider3Value(value);
    UpdateSymbolValue(
      component_id,
      MEMORY_APPLICATION_SECURE_SIZE,
      applicationSecureSymbolArray[slider3Max - value]
    );
    updateSlider5Value(UpdateSlider5Configuration(slider3Max, value));
  }
  function updateSlider4Value(value: any) {
    if (value > nSlider4RestricRange) {
      value = nSlider4RestricRange;
    }
    UpdateSliderAndBoxHeight(slider1Value, slider2Value, slider3Value);
    setSlider4Value(value);
    UpdateSymbolValue(
      component_id,
      MEMORY_BOOT_NON_SECURE_CALLABLE_SIZE,
      bootNonSecureCallableSymbolArray[value]
    );
  }
  function updateSlider5Value(value: any) {
    if (value > nSlider5RestricRange) {
      value = nSlider5RestricRange;
    }
    UpdateSliderAndBoxHeight(slider1Value, slider2Value, slider3Value);
    setSlider5Value(value);
    UpdateSymbolValue(
      component_id,
      MEMORY_APPLICATION_NON_SECURE_CALLABLE_SIZE,
      applicationNonSecureCallableSymbolArray[value]
    );
  }

  function UpdateSliderAndBoxHeight(
    slider1Value: any,
    slider2Value: any,
    slider3Value: any
  ) {
    slider2Height = GetBoxTopHeight(slider1Value, slider1Max, slider1Height);
    slider3Height = GetBoxBottomHeight(slider1Value, slider1Max, slider1Height);
    slider4Height = GetBoxTopHeight(slider2Value, slider2Max, slider2Height);
    slider5Height = GetBoxTopHeight(slider3Value, slider3Max, slider3Height);

    SetMinMax2(slider1Max, slider1Value);
    SetMinMax3(slider1Value);
    SetMinMaxSliderCallableSlider(
      slider2Max - slider2Value,
      nBootNonSecureCallableGranularity,
      bootNonSecureCallableSymbolArray.length,
      setMinMax_Slider4
    );
    SetMinMaxSliderCallableSlider(
      slider3Max - slider3Value,
      nApplicationNonSecureCallableGranularity,
      applicationNonSecureCallableSymbolArray.length,
      setMinMax_Slider5
    );
    UpdateFlashMemoryLabelValues();
  }

  function UpdateFlashMemoryLabelValues() {
    let nBytes = 0;
    let nTotal = 0;

    let bootSecureTotal = (slider2Max - slider2Value) * nBootSecureGranularity;
    let bootNonSecureCallable =
      slider4Value * nBootNonSecureCallableGranularity;
    nBytes = bootSecureTotal - bootNonSecureCallable;
    nTotal = nTotal + nBytes;
    box1Text = nBytes.toLocaleString() + ' Bytes';
    box1HexText = ByteToHex(nTotal);

    nBytes = bootNonSecureCallable;
    nTotal = nTotal + nBytes;
    box2Text = nBytes.toLocaleString() + ' Bytes';
    box2HexText = ByteToHex(nTotal);

    nBytes = slider2Value * nBootSecureGranularity;
    nTotal = nTotal + nBytes;
    box3Text = nBytes.toLocaleString() + ' Bytes';
    box3HexText = ByteToHex(nTotal);

    let applicationSecureTotal =
      (slider3Max - slider3Value) * nApplicationSecureGranularity;
    let applicationNonSecureCallable =
      slider5Value * nApplicationNonSecureCallableGranularity;

    nBytes = applicationSecureTotal - applicationNonSecureCallable;
    nTotal = nTotal + nBytes;
    box4Text = nBytes.toLocaleString() + ' Bytes';
    box4HexText = ByteToHex(nTotal);

    nBytes = applicationNonSecureCallable;
    nTotal = nTotal + nBytes;
    box5Text = nBytes.toLocaleString() + ' Bytes';
    box5HexText = ByteToHex(nTotal);

    nBytes = slider3Value * nApplicationSecureGranularity;
    nTotal = nTotal + nBytes;
    box6Text = nBytes.toLocaleString() + ' Bytes';
    box6HexText = ByteToHex(nTotal);
  }

  function getSymbolHexFormatValue(
    sliderIndex: any,
    symbolArray: any,
    symbolId: any
  ) {
    let temp = '0';
    try {
      let value = GetSymbolValue(component_id, symbolId);
      if (value == null) {
        return temp;
      }
      return symbolArray[sliderIndex];
    } catch (ex) {
      error(
        'Trustzone Manager : Max Size and Configurable Size not matching Exception: ' +
          ex
      );
      return symbolArray[symbolArray.length - 1];
    }
  }

  function GetBSOrASDiv(
    customClassName: string,
    parentSliderTopText: string,
    parentSliderBottomText: string,
    sliderTopText: string,
    sliderBottomText: string,
    parentSliderValue: any,
    parentSliderMin: any,
    parentSliderMax: any,
    parentSliderHeight: any,
    parentUpdateSliderValue: any,
    sliderValue: any,
    sliderMin: any,
    sliderMax: any,
    sliderHeight: any,
    updateSliderValue: any,
    box1Text: any,
    box1HexText: any,
    box2Text: any,
    box2HexText: any,
    box3Text: any,
    box3HexText: any,
    sliderBoxViewStatus: boolean
  ) {
    if (!sliderBoxViewStatus) {
      return;
    }
    return (
      <div className={customClassName}>
        <div style={{ paddingRight: sliderWidth }}>
          {
            //Adding slider
            GetSlider(
              parentSliderTopText,
              parentSliderBottomText,
              parentSliderValue,
              parentSliderMin,
              parentSliderMax,
              parentSliderHeight,
              parentUpdateSliderValue
            )
          }
        </div>
        <div>
          <div className="flex flex-column ">
            <div>
              {GetBNSCOrANSCDiv(
                sliderTopText,
                sliderBottomText,
                sliderValue,
                sliderMin,
                sliderMax,
                sliderHeight,
                updateSliderValue,
                box1Text,
                box1HexText,
                box2Text,
                box2HexText,
                parentSliderValue !== parentSliderMax
              )}
            </div>
            <div style={{ paddingLeft: nonSecureBoxPaddingLeft + 'px' }}>
              {
                // Adding Box
                GetBoxWithText(
                  'flex flex-row',
                  box3Text,
                  nonSecureColor,
                  GetBoxBottomHeight(
                    parentSliderValue,
                    parentSliderMax,
                    parentSliderHeight
                  ),
                  box3HexText,
                  parentSliderValue !== parentSliderMin
                )
              }
            </div>
          </div>
        </div>
      </div>
    );
  }

  function GetBNSCOrANSCDiv(
    sliderTopText: string,
    sliderBottomText: string,
    sliderValue: any,
    sliderMin: any,
    sliderMax: any,
    sliderHeight: any,
    updateSliderValue: any,
    box1Text: any,
    box1HexText: any,
    box2Text: any,
    box2HexText: any,
    sliderBoxViewStatus: boolean
  ) {
    if (!sliderBoxViewStatus) {
      return;
    }
    return (
      <div className="flex flex-row border-bottom-2">
        <div>
          {GetSlider(
            sliderTopText,
            sliderBottomText,
            sliderValue,
            sliderMin,
            sliderMax,
            sliderHeight,
            updateSliderValue
          )}
        </div>
        <div>
          <div className="flex flex-column">
            <div>
              {
                // Adding Box
                GetBoxWithText(
                  sliderValue !== sliderMax && sliderValue !== sliderMin
                    ? 'flex flex-row border-bottom-2'
                    : 'flex flex-row',
                  box1Text,
                  secureColor,
                  GetBoxTopHeight(sliderValue, sliderMax, sliderHeight),
                  box1HexText,
                  sliderValue !== sliderMax
                )
              }
            </div>
            <div>
              {
                // Adding Box
                GetBoxWithText(
                  'flex flex-row',
                  box2Text,
                  nonSecureCallableColor,
                  GetBoxBottomHeight(sliderValue, sliderMax, sliderHeight),
                  box2HexText,
                  sliderValue !== sliderMin
                )
              }
            </div>
          </div>
        </div>
      </div>
    );
  }
  return (
    <div>
      <div className="flex">
        <Fieldset className=" flash m-2" legend={flashSizeLabel}>
          <div className="flex flex-column">
            {GetTop0x0Text(topLabelPosition)}
            <div className="flex flex-row">
              <div className="border-y-2">
                {
                  //Adding slider 1
                  GetSlider(
                    'BOOTPROT',
                    'APPLICATION',
                    slider1Value,
                    slider1Min,
                    slider1Max,
                    slider1Height,
                    updateSlider1Value
                  )
                }
              </div>
              <div
                className="border-y-2"
                // style={{ width: sliderPaddingRight }}
              ></div>
              <div>
                <div className="flex flex-column border-y-2">
                  <div>
                    {GetBSOrASDiv(
                      'flex flex-row border-bottom-2',
                      'BS',
                      'BNS',
                      '',
                      'BNSC',
                      slider2Value,
                      slider2Min,
                      slider2Max,
                      slider2Height,
                      updateSlider2Value,
                      slider4Value,
                      slider4Min,
                      slider4Max,
                      slider4Height,
                      updateSlider4Value,
                      box1Text,
                      box1HexText,
                      box2Text,
                      box2HexText,
                      box3Text,
                      box3HexText,
                      slider1Value !== slider1Max
                    )}
                  </div>
                  <div>
                    {GetBSOrASDiv(
                      'flex flex-row',
                      'AS',
                      'ANS',
                      '',
                      'ANSC',
                      slider3Value,
                      slider3Min,
                      slider3Max,
                      slider3Height,
                      updateSlider3Value,
                      slider5Value,
                      slider5Min,
                      slider5Max,
                      slider5Height,
                      updateSlider5Value,
                      box4Text,
                      box4HexText,
                      box5Text,
                      box5HexText,
                      box6Text,
                      box6HexText,
                      slider1Value !== slider1Min
                    )}
                  </div>
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
