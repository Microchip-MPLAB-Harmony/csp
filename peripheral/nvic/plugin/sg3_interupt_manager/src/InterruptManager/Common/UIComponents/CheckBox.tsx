import { Checkbox } from "primereact/checkbox";
import { useState } from "react";
import { UpdateSymbolValue } from "../SymbolAccess";
import { convertToBoolean } from "../Utils";

const GetCheckBox = (props: {
  componentId: any;
  symbolId: any;
  symbolValue: string;
  styleObject: any;
  editable: boolean;
  onChange: (arg0: any) => void;
}) => {
  const [value, setValue] = useState(convertToBoolean(props.symbolValue));
  function updateValue(checked: boolean) {
    UpdateSymbolValue(props.componentId, props.symbolId, checked);
    props.onChange(checked);
    setValue(checked);
  }
  return (
    <Checkbox
      id={props.symbolId}
      inputId="binary"
      style={props.styleObject}
      checked={value}
      disabled={!props.editable}
      onChange={(e) => updateValue(e.checked)}
    />
  );
};
export default GetCheckBox;
