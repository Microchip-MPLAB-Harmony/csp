import { Dropdown } from "primereact/dropdown";
import { useState } from "react";
import { UpdateSymbolValue, AddSymbolListner } from '../SymbolAccess';
import { globalSymbolSStateData } from './UIComponentCommonUtils';

const GetDropDown = (props: {
  componentId: any;
  symbolId: any;
  symbolValue: any;
  symbolArray: any;
  styleObject: any;
  editable: boolean;
  onChange: (arg0: any) => void;
}) => {
  const [value, setValue] = useState(props.symbolValue);
  globalSymbolSStateData.set(props.symbolId,setValue);
  // AddSymbolListner(props.symbolId);
  
  function updateValue(event: { value: any }) {
    UpdateSymbolValue(props.componentId, props.symbolId, event.value);
    props.onChange(event);
    setValue(event.value);
  }

  return (
    <Dropdown
      id={props.symbolId}
      style={props.styleObject}
      value={value}
      options={props.symbolArray}
      disabled={!props.editable}
      onChange={(e) => updateValue(e)}
    />
  );
};

export default GetDropDown;
