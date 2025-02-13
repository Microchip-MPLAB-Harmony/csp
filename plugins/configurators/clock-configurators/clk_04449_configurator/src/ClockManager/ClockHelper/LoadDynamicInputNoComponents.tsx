import { InputNumberDefault } from '@mplab_harmony/harmony-plugin-client-lib';
import { Button } from 'primereact/button';


export interface ControlInputNoInterface {
  id: string;
  class: string[];
  box_id?: string;
  symbol_id?: string;
  type?: string;
  tooltip?:string;
}

export function getDynamicInputNoSymbolsFromJSON(values: ControlInputNoInterface[]) {
  return values.filter((e) => e.type === 'dynamicInputNo' && e.symbol_id !== undefined);
}


export const LoadDynamicInputNoComponents = (props: {
  componentId: string;
  dynamicSymbolsInfo: ControlInputNoInterface[];
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
            tooltip={entry?.tooltip}
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




