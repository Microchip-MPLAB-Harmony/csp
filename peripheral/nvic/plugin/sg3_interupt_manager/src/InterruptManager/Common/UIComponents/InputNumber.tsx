import { InputNumber } from "primereact/inputnumber";
import { UpdateSymbolValue } from "../SymbolAccess";

const GetInputNumber = (props: {
    componentId: any;
    symbolId: any;
    symbolValue: any;
    minFractionValue: any;
    minValue: any;
    maxValue: any;
    styleObject: any;
    editable : boolean;
    onChange: (arg0: any) => void;
  }) => {
    function updateValue(value: any) {
      UpdateSymbolValue(props.componentId, props.symbolId, value);
      props.onChange(value);
    }
  
    return (
      <InputNumber
        id={props.symbolId}
        style={props.styleObject}
        value={props.symbolValue}
        minFractionDigits={props.minFractionValue}
        maxFractionDigits={8}
        mode="decimal"
        showButtons
        min={props.minValue}
        max={props.maxValue}
        disabled = {!props.editable}
        onChange={(target) => updateValue(target.value)}
      />
    );
  }

export default GetInputNumber;
  