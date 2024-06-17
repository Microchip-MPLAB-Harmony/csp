import ControlInterface from '../Tools/ControlInterface';
import { ChangeCustomLabelComponentState, StateLabel } from '@mplab_harmony/harmony-plugin-ui';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

const FreqencyLabels = (props: {
  componentId: string;
  boxInfo: ControlInterface[];
  ChangeCustomLabelComponentState?: (symbolId: any, currentSymbolValue: any) => void;
  redColorForZeroFrequency?: boolean;
}) => {
  let onlyLabelSymbolComponents = props.boxInfo.filter(
    (e) => e.type === 'dynamic_label' && e.symbol_id !== undefined
  );

  function customLabelConfigOnSymbolChange(symbolId: unknown, currentSymbolValue: unknown) {
    if (props.ChangeCustomLabelComponentState === undefined) {
      let labelStyle = {
        color: props.redColorForZeroFrequency && currentSymbolValue === 0 ? 'red' : 'black'
      };
      ChangeCustomLabelComponentState(symbolId, currentSymbolValue, labelStyle, true, null);
    } else {
      props.ChangeCustomLabelComponentState?.(symbolId, currentSymbolValue);
    }
  }
  return (
    <div>
      {onlyLabelSymbolComponents.map((id) => (
        <StateLabel
          labelId={JSON.stringify(id.box_id)}
          labelDisplayText={GetSymbolValue(props.componentId, id.symbol_id)}
          labelSuffixText={' Hz'}
          labelStyle={{
            color:
              props.redColorForZeroFrequency &&
              GetSymbolValue(props.componentId, id.symbol_id) === 0
                ? 'red'
                : 'black'
          }}
          className={id.class[0]}
          symbolListeners={[id.symbol_id]}
          customLabelConfigOnSymbolChange={customLabelConfigOnSymbolChange}
        />
      ))}
    </div>
  );
};
export default FreqencyLabels;
