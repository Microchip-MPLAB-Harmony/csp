import { InputText } from "primereact/inputtext";
import { useState } from "react";
import { GetSymbolValue, UpdateSymbolValue } from "../SymbolAccess";

const GetInputText = (props: {
    component_id: string;
    symbolId: string;
    width : string;
    onChange: (arg0: any) => void;
    editable : boolean;
  }) => {
    const [value, setValue] = useState(GetSymbolValue(props.component_id, props.symbolId));
    function updateValue(event: { value: any }) {
      UpdateSymbolValue(props.component_id, props.symbolId, event.value);
      props.onChange(event);
      setValue(event.value);
    }
    return (
      <InputText
        id={props.symbolId}
        style={{width : props.width}}
        tooltip={value}
        value={value}
        disabled = {!props.editable}
        onChange={(e) => updateValue(e.target)}
      />
    );
  }
export default GetInputText;