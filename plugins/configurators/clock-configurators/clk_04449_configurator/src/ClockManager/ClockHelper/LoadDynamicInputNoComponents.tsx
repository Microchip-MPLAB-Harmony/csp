import { InputNumberDefault } from '@mplab_harmony/harmony-plugin-client-lib';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { Button } from 'primereact/button';


export const LoadDynamicInputNoComponents = (props: {
  componentId: string;
  dynamicSymbolsInfo: ControlInterface[];
  cx: (...classNames: string[]) => string;
  disable: boolean;
}) => {

  return (
    <div>
      {
        props.dynamicSymbolsInfo.map((entry) => (
          < InputNumberDefault
            key ={entry?.symbol_id ?? ""}
            componentId={props.componentId}
            symbolId={entry?.symbol_id ?? ""}
            className={props.cx(entry.class[0])}
            disabled ={props.disable}
          />
        ))}
    </div>
  );
};

export function GetButton(props: {
  buttonDisplayText: string;
  className: string;
  toolTip: string;
  buttonClick: (arg0: any) => void;
  disabled ?: boolean
}) {
  try {
    return (
      <Button
        aria-label='Filter'
        tooltip={props.toolTip}
        onClick={props.buttonClick}
        label={props.buttonDisplayText}
        className={props.className}
        disabled = {props?.disabled}
      />
    );
  } catch (err) {
    return <div></div>;
  }
}




