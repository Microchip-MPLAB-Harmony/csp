import { Fieldset } from 'primereact/fieldset';
import { useContext, useEffect } from 'react';
import { getIndex, nonSecureColor, secureColor } from '../MainView/TrustZoneMainView';
import { GetBoxTopHeight, GetMemoryInBytes, GetTop0x0Text, GetBoxBottomHeight } from './Memory';
import { sliderPaddingRight, TOTAL_HEIGHT, sliderWidth, boxWidth } from './Memory';
import { ByteToHex } from './MemoryLogics';
import {
  PluginConfigContext,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import GetSlider from './GetSlider';
import GetBoxWithText from './GetBoxWithText';

let previousSetValue = -1;
const DataFlashSRAM = (props: {
  fieldSetHeading: string;
  totalSize: any;
  baseGranularitySymbol: any;
  secureSymbol: any;
  nonSecureSymbol: any;
  sliderTopText: string;
  sliderBottomText: string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  useEffect(() => {}, []);

  let sliderHeight = TOTAL_HEIGHT;

  let topLabelPosition = sliderWidth + sliderPaddingRight + sliderPaddingRight + 5 + boxWidth;

  const nGranularitySymbol = useIntegerSymbol({
    componentId: componentId,
    symbolId: props.baseGranularitySymbol
  });

  const nonSecureSymbol = useKeyValueSetSymbol({
    componentId: componentId,
    symbolId: props.nonSecureSymbol
  });
  const secureSymbol = useKeyValueSetSymbol({
    componentId: componentId,
    symbolId: props.secureSymbol
  });
  let nGranularity = nGranularitySymbol.value;

  let nTotalSize = props.totalSize;

  let sliderMin = 0;
  let sliderMax = nTotalSize / nGranularity;

  let nDataSizeLabel = props.fieldSetHeading + '( ' + GetMemoryInBytes(nTotalSize) + ' )';

  let sliderValue = GetValidSliderValue(nonSecureSymbol.value);

  function updateSliderValue(value: any) {
    value = GetValidSliderValue(value);
    if (previousSetValue !== value) {
      nonSecureSymbol.writeValue(nonSecureSymbol.options[value]);
      previousSetValue = value;
    }
  }

  function GetValidSliderValue(value: number) {
    if (value > sliderMax) {
      value = sliderMax;
    } else if (value < 0) {
      value = sliderMin;
    }
    return value;
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
                <GetSlider
                  sliderTopText={props.sliderTopText}
                  sliderBottomText={props.sliderBottomText}
                  sliderValue={sliderValue}
                  sliderMin={sliderMin}
                  sliderMax={sliderMax}
                  sliderHeight={sliderHeight}
                  updateSliderValue={updateSliderValue}
                />
              </div>
              <div className='flex flex-column '>
                <div>
                  <GetBoxWithText
                    classCustom={
                      sliderValue !== sliderMax && sliderValue !== sliderMin
                        ? 'flex flex-row border-bottom-2'
                        : 'flex flex-row'
                    }
                    displayText={secureSymbol.selectedOption}
                    color={secureColor}
                    boxHeight={GetBoxTopHeight(sliderValue, sliderMax, sliderHeight)}
                    hexDisplayText={ByteToHex(secureSymbol.value * nGranularity)}
                    textDisplayStatus={sliderValue !== sliderMax}
                  />
                </div>
                <div>
                  <GetBoxWithText
                    classCustom={'flex flex-row'}
                    displayText={nonSecureSymbol.options[sliderValue]}
                    color={nonSecureColor}
                    boxHeight={GetBoxBottomHeight(sliderValue, sliderMax, sliderHeight)}
                    hexDisplayText={ByteToHex(sliderMax * nGranularity)}
                    textDisplayStatus={sliderValue !== sliderMin}
                  />
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
