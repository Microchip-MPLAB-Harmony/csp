import {
  DefaultControl,
  PluginConfigContext,
  symbolUtilApi
} from '@mplab_harmony/harmony-plugin-client-lib';
import { ConfigSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext, useEffect, useState } from 'react';
import styles from './input-scan.module.css';

async function getInputScanSymbols(componentId: string) {
  const children = await symbolUtilApi.getChildren(componentId, 'AD1CON2__CSCNA');

  if (children.length > 0) {
    const symbols: ConfigSymbol<any>[] = (await symbolUtilApi.getSymbols(
      componentId,
      children
    )) as ConfigSymbol<any>[];

    return symbols
      .filter((symbol) => symbol.symbolType === 'BooleanSymbol' && symbol.symbolId.includes('CSSL'))
      .map((symbol) => {
        symbol.label = symbol.label.replace('Select ', '').replace(' for Input Scan', '');
        return symbol;
      });
  } else {
    return [] as ConfigSymbol<any>[];
  }
}

function InputScanConfiguration() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);
  const [inputScanSymbols, setInputScanSymbols] = useState<ConfigSymbol<any>[]>([]);

  useEffect(() => {
    getInputScanSymbols(componentId).then(setInputScanSymbols);
    return () => {};
  }, []);

  return (
    <div className={styles['input-scan-configuration-container']}>
      {inputScanSymbols.map((symbol) => (
        <div
          style={{ display: 'flex', justifyContent: 'flex-end' }}
          key={symbol.symbolId}>
          <label style={{ textAlign: 'right', paddingRight: '10px' }}>{symbol.label}</label>
          <DefaultControl symbol={symbol}></DefaultControl>
        </div>
      ))}
    </div>
  );
}

export { getInputScanSymbols };

export default InputScanConfiguration;
