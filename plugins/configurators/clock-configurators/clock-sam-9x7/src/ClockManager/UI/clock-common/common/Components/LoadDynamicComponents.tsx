import { GetUIComponentWithOutLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import ControlInterface from '../Tools/ControlInterface';

const LoadDynamicComponents = (props: {
  componentId: string;
  boxInfo: ControlInterface[];
  onChange?: (onChangeData: Map<String, any>) => void;
}) => {
  let onlyNonLabelSymbolComponents = props.boxInfo.filter(
    (e) => e.type === 'dynamic' && e.symbol_id !== undefined
  );
  function symbolValueChanged(onchangeData: Map<String, any>) {
    props.onChange?.(onchangeData);
  }
  return (
    <div>
      {onlyNonLabelSymbolComponents.map((id) => (
        <GetUIComponentWithOutLabel
          componentId={props.componentId}
          symbolId={id.symbol_id}
          className={id.class[0]}
          symbolListeners={[id.symbol_id]}
          onChange={symbolValueChanged}
        />
      ))}
    </div>
  );
};
export default LoadDynamicComponents;
