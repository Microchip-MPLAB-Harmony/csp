import ControlInterface from '../../Tools/ControlInterface';
import { DefaultControl, ISymbol, symbolUtilApi } from '@mplab_harmony/harmony-plugin-client-lib';
import { useEffect, useState } from 'react';

const LoadDynamicComponents = (props: {
  componentId: string;
  dynamicSymbolsInfo: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const [symbols, setSymbols] = useState<ISymbol[]>([]);
  useEffect(() => {
    const symbolIDs = props.dynamicSymbolsInfo.map((e) => e.symbol_id) as string[];
    symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e: ISymbol[]) => {
      setSymbols(e);
    });
  }, []);
  return (
    <div>
      {symbols.length !== 0 &&
        props.dynamicSymbolsInfo.map((id, index) => (
          <DefaultControl
            key={id.id}
            symbol={symbols[index]}
            className={props.cx(id.class[0])}
          />
        ))}
    </div>
  );
};

export default LoadDynamicComponents;
