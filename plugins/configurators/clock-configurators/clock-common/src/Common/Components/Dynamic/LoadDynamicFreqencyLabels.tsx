<<<<<<< HEAD
import { useEffect, useState } from 'react';
import ControlInterface from '../../Tools/ControlInterface';
import { ISymbol, symbolUtilApi } from '@mplab_harmony/harmony-plugin-client-lib';
import FrequencyLabelBySymbolType from '../LabelComponent/LabelFreqTools/FrequencyLabelBySymbolType';
=======
import ControlInterface from '../../Tools/ControlInterface';
import LabelComponent from '../LabelComponent/FrequencyLabelComponent';
>>>>>>> 0d345d5887 (Added HTML clock manager PIC32CM_GC_SG supported devices)

const LoadDynamicFreqencyLabels = (props: {
  componentId: string;
  dynamicLabelSymbolsInfo: ControlInterface[];
  cx: (...classNames: string[]) => string;
  boldLabelStatus?: boolean;
  toolTip?: string;
  redColorForZeroFrequency?: boolean;
}) => {
<<<<<<< HEAD
  const [symbols, setSymbols] = useState<ISymbol[]>([]);
  useEffect(() => {
    const symbolIDs = props.dynamicLabelSymbolsInfo.map((e) => e.symbol_id) as string[];
    symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e: ISymbol[]) => {
      setSymbols(e);
    });
  }, []);
  return (
    <div>
      {symbols.length !== 0 &&
        props.dynamicLabelSymbolsInfo.map((id, index) => (
          <FrequencyLabelBySymbolType
            key={id.id}
            componentId={props.componentId}
            symbolId={symbols[index].symbolId}
            className={props.cx(id.class[0])}
            boldLabelStatus={props.boldLabelStatus}
            tooltip={props.toolTip}
            redColorForZeroFrequency={props.redColorForZeroFrequency}
            symbolType={symbols[index].symbolType}
=======
  const symbolIDs = props.dynamicLabelSymbolsInfo.map((e) => e.symbol_id) as string[];
  return (
    <div>
      {symbolIDs.length !== 0 &&
        props.dynamicLabelSymbolsInfo.map((id, index) => (
          <LabelComponent
            key={id.id}
            componentId={props.componentId}
            symbolId={symbolIDs[index]}
            class={props.cx(id.class[0])}
            boldLabelStatus={props.boldLabelStatus}
            redColorForZeroFrequency={props.redColorForZeroFrequency}
>>>>>>> 0d345d5887 (Added HTML clock manager PIC32CM_GC_SG supported devices)
          />
        ))}
    </div>
  );
};
export default LoadDynamicFreqencyLabels;
