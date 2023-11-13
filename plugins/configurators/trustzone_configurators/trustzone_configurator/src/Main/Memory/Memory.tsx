import { Slider } from 'primereact/slider';
// import FlashMemory from './FlashMemory';
import { nonSecureColor } from '../MainView/TrustZoneMainView';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  component_id,
  secureColor,
  nonSecureCallableColor,
} from '../MainView/TrustZoneMainView';
import DataFlashSRAM from './DataFlashSRAM';
import FlashMemory from './FlashMemory';

let screenHeight = window.screen.availHeight;
let heightFactor = screenHeight / 824;
export let TOTAL_HEIGHT = 45 * heightFactor;
export let boxWidth = 170;
export let sliderPaddingRight = 60;
export let boxRightSideTempWidth = 100;
export let boxpaddingLeft = 60;
export let sliderWidth = 2;

const Memory = () => {
  return (
    <div>
      <div className="flex">
        <div>
          <FlashMemory />
        </div>
        <div>
          <DataFlashSRAM
            fieldSetHeading={'DATA FLASH'}
            totalSizeSymbol={'DEVICE_DATAFLASH_SIZE'}
            baseGranularitySymbol={'IDAU_DS_GRANULARITY'}
            secureSymbol={'IDAU_DS_SIZE'}
            sliderTopText={'DS'}
            sliderBottomText={'DNS'}
          />
        </div>
        <div>
          <DataFlashSRAM
            fieldSetHeading={'SRAM'}
            totalSizeSymbol={'DEVICE_RAM_SIZE'}
            baseGranularitySymbol={'IDAU_RS_GRANULARITY'}
            secureSymbol={'IDAU_RS_SIZE'}
            sliderTopText={'RS'}
            sliderBottomText={'RNS'}
          />
        </div>
        <div>{GetColorNote(20, 'flex flex-column gap-2')}</div>
      </div>
    </div>
  );
};
export default Memory;

function GetDivColorAndText(color: any, text: any, size: any) {
  return (
    <div>
      <div className="flex flex-row gap-2">
        <div
          style={{
            backgroundColor: color,
            width: size + 'px',
            height: size + 'px',
          }}
        ></div>
        <div>{text}</div>
      </div>
    </div>
  );
}

export function GetColorNote(size: any, flexdirect: any) {
  return (
    <div>
      <div className={flexdirect}>
        <div>Color Note :</div>
        <div>{GetDivColorAndText(secureColor, 'Secure', size)}</div>
        <div>
          {GetDivColorAndText(
            nonSecureCallableColor,
            'Non-Secure Callable',
            size
          )}
        </div>
        <div>{GetDivColorAndText(nonSecureColor, 'Non-Secure', size)}</div>
      </div>
    </div>
  );
}

export function GetSlider(
  sliderTopText: string,
  sliderBottomText: string,
  sliderValue: any,
  sliderMin: any,
  sliderMax: any,
  sliderHeight: any,
  setSliderValue: (arg0: any) => void
) {
  let topTextHeight = GetBoxTopHeight(sliderValue, sliderMax, sliderHeight);
  let bottomTextHeight = GetBoxBottomHeight(
    sliderValue,
    sliderMax,
    sliderHeight
  );
  let bTopTextVisibleStatus = sliderValue !== sliderMax;
  let bBottomTextVisibleStatus = sliderValue !== sliderMin;
  return (
    <div className="flex flex-row">
      <div>
        <div className="flex flex-column flex justify-content-center flex-wrap card-container">
          <div
            className="flex align-items-center justify-content-center"
            style={{
              width: sliderPaddingRight,
              height: topTextHeight + 'rem',
            }}
          >
            <div style={{ transform: 'rotate(-90deg)' }}>
              {bTopTextVisibleStatus && sliderTopText}
            </div>
          </div>
          <div
            className="flex align-items-center justify-content-center"
            style={{
              width: sliderPaddingRight,
              height: bottomTextHeight + 'rem',
            }}
          >
            <div style={{ transform: 'rotate(-90deg)' }}>
              {bBottomTextVisibleStatus && sliderBottomText}
            </div>
          </div>
        </div>
      </div>
      <div>
        <Slider
          value={sliderValue}
          min={sliderMin}
          max={sliderMax}
          style={{ height: sliderHeight + 'rem', width: sliderWidth + 'px' }}
          onChange={(e: any) => setSliderValue(e.value)}
          orientation="vertical"
        />
      </div>
    </div>
  );
}

export function GetBox(
  boxtText: any,
  boxColor: any,
  boxHeight: any,
  paddingleftValue: any,
  textDisplayStatus: any
) {
  return (
    <div
      className="flex justify-content-center flex-wrap card-container"
      style={{ paddingLeft: paddingleftValue + 'px' }}
    >
      <div
        className="flex align-items-center justify-content-center hover:text-white text-gray-900 text-lg"
        style={{
          backgroundColor: boxColor,
          height: boxHeight + 'rem',
          width: boxWidth + 'px',
        }}
      >
        {textDisplayStatus && boxtText}
      </div>
    </div>
  );
}

export function GetBoxBottomHeight(
  sliderValue: any,
  sliderMax: any,
  nTotalHeight: any
) {
  return (sliderValue / sliderMax) * nTotalHeight;
}

export function GetBoxTopHeight(
  sliderValue: any,
  sliderMax: any,
  nTotalHeight: any
) {
  return ((sliderMax - sliderValue) / sliderMax) * nTotalHeight;
}

export function GetMemoryInBytes(bytes: any) {
  return bytes + ' Bytes';
}

export function GetGranularityFactor(
  symboID: string,
  nBaseGranularity: number
) {
  let value = GetSymbolValue(component_id, symboID);
  if (value == null) {
    return 0;
  }
  return nBaseGranularity / value;
}

export function GetBoxWithText(
  classCustom: any,
  displayText: any,
  color: any,
  boxHeight: any,
  hexDisplayText: any,
  textDisplayStatus: any
) {
  return (
    <div className={classCustom}>
      {GetBox(displayText, color, boxHeight, boxpaddingLeft, textDisplayStatus)}
      {textDisplayStatus && (
        <div
          className="flex align-items-end justify-content-start text-gray-900 text-lg"
          style={{
            width: boxRightSideTempWidth + 'px',
            height: boxHeight + 'rem',
            paddingLeft: '5px',
          }}
        >
          {hexDisplayText}
        </div>
      )}
    </div>
  );
}

export function GetTop0x0Text(topLabelPosition: any) {
  return (
    <div className="flex">
      <div style={{ width: topLabelPosition + 'px' }}></div>
      <div className="flex justify-content-start text-gray-900 text-lg">
        0x0{' '}
      </div>
    </div>
  );
}
