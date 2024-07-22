import {
  ConfigSymbol,
  symbolApi,
  useHexSymbol,
  useKeyValueSetSymbol,
  useStringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service';
import { Slider } from 'primereact/slider';
import { useEffect, useState } from 'react';

const Component = () => {
  // const [symbols, setSymbols] = useState<ConfigSymbol<any>>();
  useEffect(() => {
    // symbolApi.getSymbol('core', 'DEVICE_RAM_SIZE').then((e: ConfigSymbol<any>) => {
    //   setSymbols(e);
    // });
  }, []);
  const data = useKeyValueSetSymbol({ componentId: 'core', symbolId: 'IDAU_RNS_SIZE' });
  let sliderValue = GetValidSliderValue(data.value);
  // let nSRAMTotalSize = GetSymbolValue('core', 'IDAU_RNS_SIZE');
  function GetValidSliderValue(value: any) {
    if (value > data.options.length - 1) {
      value = data.options.length - 1;
    } else if (value < 0) {
      value = 0;
    }
    return value;
  }
  function UpdateValue(value: any) {
    if (value < 0) {
      return;
    }
    data.writeValue(value);
  }
  console.log(GetValidSliderValue(data.value));
  return (
    <div>
      <Slider
        value={sliderValue}
        onChange={(e: any) => UpdateValue(GetValidSliderValue(e))}
      />
    </div>
  );
};
export default Component;
