import { Fieldset } from 'primereact/fieldset';
import { useEffect, useState } from 'react';
import { nonSecureColor, secureColor, component_id } from '../MainView/TrustZoneMainView';
import '../../Styles/memory.css';
import { getIndex } from '@mplab_harmony/harmony-plugin-ui/build/utils/CommonUtil';
import {
  AddSymbolListener,
  GetSymbolArray,
  GetSymbolValue
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  GetBoxBottomHeight,
  GetBoxTopHeight,
  GetBoxWithText,
  GetMemoryInBytes,
  GetTop0x0Text
} from './Memory';
import { GetSlider, sliderPaddingRight, TOTAL_HEIGHT, sliderWidth, boxWidth } from './Memory';
import { UpdateSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { ByteToHex, SetSliderValueLowerValueSymbolType } from './MemoryLogics';
import { GetValidSilderSymbolValue } from './MemoryLogics';
import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import { ConfigSymbolEvent } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';

const DataFlashSRAM = (props: {
  fieldSetHeading: string;
  totalSizeSymbol: any;
  baseGranularitySymbol: any;
  secureSymbol: any;
  nonSecureSymbol: any;
  sliderTopText: string;
  sliderBottomText: string;
}) => {
  useEffect(() => {
    addSymbolListeneres();
  }, []);
  function addSymbolListeneres() {
    addListener(props.nonSecureSymbol);
    addListener(props.secureSymbol);
  }

  function addListener(symbolId: string) {
    AddSymbolListener(symbolId);
    globalSymbolSStateData.set(symbolId, {
      symbolChanged: symbolChanged
    });
  }

  const symbolChanged = (symbol: ConfigSymbolEvent) => {
    switch (symbol.symbolID) {
      case props.secureSymbol:
        setSecureValue(Number(getIndex(symbol.value, secureSymbolArray)));
        break;
      case props.nonSecureSymbol:
        setSliderValue(getIndex(symbol.value, nonSecureSymbolArray));
        break;
    }
  };

  let sliderHeight = TOTAL_HEIGHT;

  let topLabelPosition = sliderWidth + sliderPaddingRight + sliderPaddingRight + 5 + boxWidth;

  let nGranularity = GetSymbolValue(component_id, props.baseGranularitySymbol);
  let nonSecureSymbolArray = GetSymbolArray(component_id, props.nonSecureSymbol);
  let secureSymbolArray = GetSymbolArray(component_id, props.secureSymbol);

  let nTotalSize = GetSymbolValue(component_id, props.totalSizeSymbol);
  let sliderMin = 0;
  let sliderMax = secureSymbolArray.length - 1;
  let nSliderRestricRange = nonSecureSymbolArray.length - 1;

  let nDataSizeLabel = props.fieldSetHeading + '( ' + GetMemoryInBytes(nTotalSize) + ' )';

  let symbolValue = getIndex(
    GetValidSilderSymbolValue(props.nonSecureSymbol, sliderMax, nSliderRestricRange),
    nonSecureSymbolArray
  );

  const [sliderValue, setSliderValue] = useState<number | number>(
    SetSliderValueLowerValueSymbolType(symbolValue, sliderMax)
  );
  const [secureValue, setSecureValue] = useState<number | number>(
    getIndex(GetSymbolValue(component_id, props.secureSymbol), secureSymbolArray)
  );
  function updateSliderValue(value: any) {
    if (value > nSliderRestricRange) {
      value = nSliderRestricRange;
    }
    setSliderValue(value);
    UpdateSymbolValue(component_id, props.nonSecureSymbol, nonSecureSymbolArray[value]);
  }

  return (
    <div className='flex'>
      <Fieldset
        className=' dataflash m-2'
        legend={nDataSizeLabel}>
        <div className='flex flex-column '>
          {GetTop0x0Text(topLabelPosition)}
          <div>
            <div className='flex flex-row border-y-2'>
              <div>
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
              <div className='flex flex-column '>
                <div>
                  {GetBoxWithText(
                    sliderValue !== sliderMax && sliderValue !== sliderMin
                      ? 'flex flex-row border-bottom-2'
                      : 'flex flex-row',
                    secureSymbolArray[secureValue],
                    secureColor,
                    GetBoxTopHeight(sliderValue, sliderMax, sliderHeight),
                    ByteToHex(secureValue * nGranularity),
                    sliderValue !== sliderMax
                  )}
                </div>
                <div>
                  {GetBoxWithText(
                    'flex flex-row',
                    nonSecureSymbolArray[sliderValue],
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
