import { useEffect, useState } from 'react';
import ControlInterface from '../../Tools/ControlInterface';
import LabelComponent from './FrequencyLabelComponent';
import { ISymbol, symbolUtilApi } from '@mplab_harmony/harmony-plugin-client-lib';

const FreqencyLabels = (props: {
  componentId: string;
  boxInfo: ControlInterface[];
  cx: (...classNames: string[]) => string;
  boldLabelStatus?: boolean;
  redColorForZeroFrequency?: boolean;
}) => {
  const [symbols, setSymbols] = useState<ISymbol[]>([]);
  useEffect(() => {
    const symbolIDs = props.boxInfo.map((e) => e.symbol_id) as string[];
    symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e: ISymbol[]) => {
      setSymbols(e);
    });
  }, []);
  return (
    <div>
      {symbols.length !== 0 &&
        props.boxInfo.map((id, index) => (
          <LabelComponent
            key={id.id}
            componentId={props.componentId}
            symbolId={symbols[index].symbolId}
            class={props.cx(id.class[0])}
            boldLabelStatus={props.boldLabelStatus}
            redColorForZeroFrequency={props.redColorForZeroFrequency}
          />
        ))}
    </div>
  );
};
export default FreqencyLabels;
