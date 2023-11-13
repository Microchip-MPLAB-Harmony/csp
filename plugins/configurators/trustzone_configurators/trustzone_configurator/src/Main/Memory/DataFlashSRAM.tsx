import { Fieldset } from 'primereact/fieldset';
import { useState } from 'react';
import {
  nonSecureColor,
  secureColor,
  component_id,
} from '../MainView/TrustZoneMainView';
import '../../Styles/memory.css';
import { getIndex } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import {
  GetSymbolArray,
  GetSymbolValue,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  GetBoxBottomHeight,
  GetBoxTopHeight,
  GetBoxWithText,
  GetMemoryInBytes,
  GetTop0x0Text,
} from './Memory';
import {
  GetSlider,
  sliderPaddingRight,
  TOTAL_HEIGHT,
  sliderWidth,
  boxWidth,
} from './Memory';
import { UpdateSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { ByteToHex } from './MemoryLogics';
import {
  GetValidSilderSymbolValue,
  SetSliderValueUpperValueSymbolType,
} from './MemoryLogics';

const DataFlashSRAM = (props: {
  fieldSetHeading: string;
  totalSizeSymbol: any;
  baseGranularitySymbol: any;
  secureSymbol: any;
  sliderTopText: string;
  sliderBottomText: string;
}) => {
  let sliderHeight = TOTAL_HEIGHT;

  let topLabelPosition =
    sliderWidth + sliderPaddingRight + sliderPaddingRight + 5 + boxWidth;

  let nGranularity = GetSymbolValue(component_id, props.baseGranularitySymbol);
  let secureSymbolArray = GetSymbolArray(component_id, props.secureSymbol);

  let nTotalSize = GetSymbolValue(component_id, props.totalSizeSymbol);
  let sliderMin = 0;
  let sliderMax = nTotalSize / nGranularity;
  let nSliderRestricRange = sliderMax;

  let nDataSizeLabel =
    props.fieldSetHeading + '( ' + GetMemoryInBytes(nTotalSize) + ' )';

  let symbolValue = getIndex(
    GetValidSilderSymbolValue(
      props.secureSymbol,
      sliderMax,
      nSliderRestricRange
    ),
    secureSymbolArray
  );

  const [sliderValue, setSliderValue] = useState<number | number>(
    SetSliderValueUpperValueSymbolType(symbolValue, sliderMax)
  );
  function updateSliderValue(value: any) {
    UpdateSymbolValue(
      component_id,
      props.secureSymbol,
      secureSymbolArray[value]
    );
    setSliderValue(value);
  }

  return (
    <div className="flex">
      <Fieldset className=" dataflash m-2" legend={nDataSizeLabel}>
        <div className="flex flex-column ">
          {GetTop0x0Text(topLabelPosition)}
          <div>
            <div className="flex flex-row border-y-2">
              <div
                style={
                  {
                    // paddingRight: '30px',
                    // paddingLeft: sliderPaddingRight + 'px',
                  }
                }
              >
                {GetSlider(
                  props.sliderTopText,
                  props.sliderBottomText,
                  sliderValue,
                  sliderMin,
                  sliderMax,
                  sliderHeight,
                  updateSliderValue
                )}
              </div>
              <div className="flex flex-column ">
                <div>
                  {GetBoxWithText(
                    sliderValue !== sliderMax && sliderValue !== sliderMin
                      ? 'flex flex-row border-bottom-2'
                      : 'flex flex-row',
                    secureSymbolArray[sliderMax - sliderValue],
                    secureColor,
                    GetBoxTopHeight(sliderValue, sliderMax, sliderHeight),
                    ByteToHex((sliderMax - sliderValue) * nGranularity),
                    sliderValue !== sliderMax
                  )}
                </div>
                <div>
                  {GetBoxWithText(
                    'flex flex-row',
                    secureSymbolArray[sliderValue],
                    nonSecureColor,
                    GetBoxBottomHeight(sliderValue, sliderMax, sliderHeight),
                    ByteToHex(sliderMax * nGranularity),
                    sliderValue !== sliderMin
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </Fieldset>
    </div>
  );
};
export default DataFlashSRAM;
