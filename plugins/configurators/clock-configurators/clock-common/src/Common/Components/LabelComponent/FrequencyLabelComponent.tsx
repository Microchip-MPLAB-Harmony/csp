import { ISymbol, SymbolProps, symbolUtilApi } from '@mplab_harmony/harmony-plugin-client-lib';
import { useEffect, useState } from 'react';
import FrequencyLabelBySymbolType from './LabelFreqTools/FrequencyLabelBySymbolType';
export interface LabelProps {
  className: string;
  boldLabelStatus?: boolean;
  tooltip?: string;
  redColorForZeroFrequency?: boolean;
  minMaxOutofRangeRedColorStatus?: boolean;
}

const FrequencyLabelComponent = (props: SymbolProps & LabelProps) => {
  const [symbols, setSymbols] = useState<ISymbol[]>([]);
  useEffect(() => {
    const symbolIDs = [props.symbolId];
    symbolUtilApi.getSymbolTypes(props.componentId, symbolIDs).then((e: ISymbol[]) => {
      setSymbols(e);
    });
  }, []);
  return (
    <div>
      {symbols.length !== 0 && (
        <FrequencyLabelBySymbolType
          symbolType={symbols[0].symbolType}
          {...props}
        />
      )}
    </div>
  );
};
export default FrequencyLabelComponent;
