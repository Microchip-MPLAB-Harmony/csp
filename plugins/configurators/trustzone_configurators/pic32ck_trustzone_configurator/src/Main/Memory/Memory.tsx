import { nonSecureColor } from '../MainView/TrustZoneMainView';
import { secureColor, nonSecureCallableColor } from '../MainView/TrustZoneMainView';
import DataFlashSRAM from './DataFlashSRAM';
import FlashMemory from './FlashMemory';
import {
  ConfigSymbol,
  PluginConfigContext,
  symbolApi,
  useIntegerSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext, useEffect, useState } from 'react';

let screenHeight = window.screen.availHeight;
let heightFactor = screenHeight / 824;
export let TOTAL_HEIGHT = 53 * heightFactor;
export let boxWidth = 200;
export let sliderPaddingRight = 60;
export let boxRightSideTempWidth = 100;
export let boxpaddingLeft = 60;
export let sliderWidth = 2;

const Memory = () => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [deviceFlashSizeSymbol, setDeviceFlashSizeSymbol] = useState<ConfigSymbol<any>>();
  const [nSRAMTotalSizeSymbol, setNSRAMTotalSizeSymbol] = useState<ConfigSymbol<any>>();
  useEffect(() => {
    symbolApi.getSymbol(componentId, 'DEVICE_DATAFLASH_SIZE').then((e: ConfigSymbol<any>) => {
      setDeviceFlashSizeSymbol(e);
    });
    symbolApi.getSymbol(componentId, 'DEVICE_RAM_SIZE').then((e: ConfigSymbol<any>) => {
      setNSRAMTotalSizeSymbol(e);
    });
  }, [componentId]);

  return (
    <div>
      <div className='flex'>
        <div>
          <FlashMemory />
        </div>
        <div>
          {deviceFlashSizeSymbol?.value !== undefined && deviceFlashSizeSymbol.value !== 0 && (
            <DataFlashSRAM
              key={'IDAU_DNS_SIZE'}
              fieldSetHeading={'DATA FLASH'}
              totalSize={deviceFlashSizeSymbol.value}
              baseGranularitySymbol={'IDAU_DNS_GRANULARITY'}
              secureSymbol={'IDAU_DS_SIZE'}
              nonSecureSymbol={'IDAU_DNS_SIZE'}
              sliderTopText={'DS'}
              sliderBottomText={'DNS'}
            />
          )}
        </div>
        <div>
          {nSRAMTotalSizeSymbol?.value !== undefined && nSRAMTotalSizeSymbol.value !== 0 && (
            <DataFlashSRAM
              key={'IDAU_RNS_SIZE'}
              fieldSetHeading={'SRAM'}
              totalSize={nSRAMTotalSizeSymbol.value}
              baseGranularitySymbol={'IDAU_RNS_GRANULARITY'}
              secureSymbol={'IDAU_RS_SIZE'}
              nonSecureSymbol={'IDAU_RNS_SIZE'}
              sliderTopText={'RS'}
              sliderBottomText={'RNS'}
            />
          )}
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
      <div className='flex flex-row gap-2'>
        <div
          style={{
            backgroundColor: color,
            width: size + 'px',
            height: size + 'px'
          }}></div>
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
        <div>{GetDivColorAndText(nonSecureCallableColor, 'Non-Secure Callable', size)}</div>
        <div>{GetDivColorAndText(nonSecureColor, 'Non-Secure', size)}</div>
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
      className='flex justify-content-center flex-wrap card-container'
      style={{ paddingLeft: paddingleftValue + 'px' }}>
      <div
        className='flex align-items-center justify-content-center hover:text-white text-center text-gray-900 text-lg'
        style={{
          backgroundColor: boxColor,
          height: boxHeight + 'rem',
          width: boxWidth + 'px'
        }}>
        {textDisplayStatus && (
          <label
            style={{ padding: '15px' }}
            title={boxtText}>
            {boxtText}
          </label>
        )}
      </div>
    </div>
  );
}

export function GetBoxBottomHeight(sliderValue: any, sliderMax: any, nTotalHeight: any) {
  return (sliderValue / sliderMax) * nTotalHeight;
}

export function GetBoxTopHeight(sliderValue: any, sliderMax: any, nTotalHeight: any) {
  return ((sliderMax - sliderValue) / sliderMax) * nTotalHeight;
}

export function GetMemoryInBytes(bytes: any) {
  bytes = isHexadecimal(bytes) ? parseInt(bytes, 16) : bytes;
  return bytes + ' Bytes';
}

function isHexadecimal(str: string): boolean {
  // Regular expression to match a valid hexadecimal string
  const hexRegEx = /^(0x|0X)[0-9a-fA-F]+$/;
  return hexRegEx.test(str);
}

export function GetGranularityFactor(symboID: string, nBaseGranularity: number) {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const symbol = useIntegerSymbol({ componentId: componentId, symbolId: symboID });
  let value = symbol.value;
  if (value == null) {
    return 0;
  }
  return nBaseGranularity / value;
}

export function GetTop0x0Text(topLabelPosition: any) {
  return (
    <div className='flex'>
      <div style={{ width: topLabelPosition + 'px' }}></div>
      <div className='flex justify-content-start text-gray-900 text-lg'>0x0 </div>
    </div>
  );
}
