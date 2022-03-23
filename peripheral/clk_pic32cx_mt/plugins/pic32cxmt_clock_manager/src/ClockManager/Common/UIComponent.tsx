import { Checkbox } from "primereact/checkbox";
import { Dropdown } from "primereact/dropdown";
import { InputNumber } from "primereact/inputnumber";
import { stringify } from "querystring";

import {
  GetSymbolArray,
  GetSymbolValue,
  GetSymbolLabelName,
  GetSymbolMinValue,
  GetSymbolMaxValue,
  GetSymbolType,
  GetSymbolVisibleStatus,
  UpdateSymbolValue,
} from "./SymbolAccess";
import { convertToBoolean } from "./Utils";
import { toolBarHeight } from "../UI/MainView/MainBlock";
import { Button } from "primereact/button";

export let globalSymbolStyleData = new Map<any, Map<string, string>>();

let defaultInputNumberStyleMap = new Map<any, any>();
defaultInputNumberStyleMap.set("width", "8rem");
defaultInputNumberStyleMap.set("height", "1.7rem");
defaultInputNumberStyleMap.set("fontSize", "12px");

let defaultDropDownStyleMap = new Map<any, any>();
defaultDropDownStyleMap.set("height", "2.3rem");
defaultDropDownStyleMap.set("fontSize", "14px");

interface LabelProps {
  labelName: any;
}

interface CustomLabel {
  labelId: string;
  labelDisplayText: string;
  labelStyle : any;
}

interface CustomLabelWithTooltip {
  labelId: string;
  labelDisplayText: string;
  labelTooltip : string;
  labelStyle : any;
}

export enum SymbolType {
  DropDown,
  InputNumber,
  CheckBox,
  String,
}

function Component(props: {
  componentId: any;
  symbolId: any;
  onChange: (arg0: any) => void;
}) {
  let component = null;
  let value = GetSymbolValue(props.componentId, props.symbolId);
  if (value === null) {
    alert("Missing_Symbol: " + props.symbolId);
    return null;
  }

  let symbolVisibleStatus =
    GetSymbolVisibleStatus(props.componentId, props.symbolId) === true
      ? true
      : false;
  if (!symbolVisibleStatus) {
    return null;
  }

  let symbolType = GetComponentType({
    componentId: props.componentId,
    symbolID: props.symbolId,
  });

  switch (symbolType) {
    case SymbolType.DropDown:
      component = (
        <GetDropDown
          componentId={props.componentId}
          symbolId={props.symbolId}
          symbolValue={value}
          symbolArray={GetSymbolArray(props.componentId, props.symbolId)}
          styleObject={GetDropDownStyle(props.symbolId)}
          onChange={(target) => props.onChange(target.target)}
        />
      );
      break;
    case SymbolType.InputNumber:
      component = (
        <GetInputNumber
          componentId={props.componentId}
          symbolId={props.symbolId}
          symbolValue={value}
          minFractionValue={GetMinFractionValueBasedSymbolType(
            props.componentId,
            props.symbolId
          )}
          minValue={GetSymbolMinValue(props.componentId, props.symbolId)}
          maxValue={GetSymbolMaxValue(props.componentId, props.symbolId)}
          styleObject={GetInputNumberStyle(props.symbolId)}
          onChange={(target) => props.onChange(target.target)}
        />
      );
      break;
    case SymbolType.CheckBox:
      component = (
        <GetCheckBox
          componentId={props.componentId}
          symbolId={props.symbolId}
          symbolValue={value}
          styleObject={GetStyle(props.symbolId)}
          onChange={(target) => props.onChange(target.target)}
        />
      );
      break;
    case SymbolType.String:
      component = (
        <div className="p-text-italic">
          <DisplayLabel labelName={value} />
        </div>
      );
      break;
    default:
      alert("Invalid SymbolType.");
  }
  return component;
}

function ComponentWithLabel(props: {
  componentId: any;
  symbolId: any;
  onChange: (arg0: any) => void;
}) {
  let component = Component(props);
  if (component === null) {
    return null;
  }
  return (
    <div>
      <div className="p-field p-grid">
        <DisplayLabel
          labelName={GetSymbolLabelName(props.componentId, props.symbolId)}
        />{" "}
        <div className="p-col">{component}</div>
      </div>
    </div>
  );
}

function ComponentWithOutLabel(props: {
  componentId: any;
  symbolId: any;
  onChange: (arg0: any) => void;
}) {
  return (
    <div>
      <Component
        componentId={props.componentId}
        symbolId={props.symbolId}
        onChange={props.onChange}
      />
    </div>
  );
}

export function GetMinFractionValueBasedSymbolType(componentId: any, symbolID: any) {
  let typeofSymbol = GetSymbolType(componentId, symbolID);
  if (typeofSymbol === "Float") {
    return 1;
  }
  return 0;
}

function GetComponentType(props: { componentId: any; symbolID: any }) {
  let typeofSymbol = GetSymbolType(props.componentId, props.symbolID);
  let type = null;
  switch (typeofSymbol) {
    case "Boolean":
      type = SymbolType.CheckBox;
      break;
    case "Integer":
    case "Long":
    case "Hex":
    case "Float":
      type = SymbolType.InputNumber;
      break;
    case "KeyValueSet":
    case "ComboSymbol":
    case "Combo":
      type = SymbolType.DropDown;
      break;
    case "String":
      type = SymbolType.String;
      break;
    default:
      alert("Invalid SymbolType " + props.symbolID);
  }
  return type;
}

export function GetUIComponentWithLabel(props: {
  componentId: any;
  symbolId: any;
  onChange: (arg0: any) => void;
}) {
  return (
    <div>
      <ComponentWithLabel
        componentId={props.componentId}
        symbolId={props.symbolId}
        onChange={props.onChange}
      />
    </div>
  );
}

export function GetUIComponentWithOutLabel(props: {
  componentId: any;
  symbolId: any;
  onChange: (arg0: any) => void;
}) {
  return (
    <div>
      <ComponentWithOutLabel
        componentId={props.componentId}
        symbolId={props.symbolId}
        onChange={props.onChange}
      />
    </div>
  );
}

const DisplayLabel: React.FC<LabelProps> = (props): JSX.Element => (
  <>
    <label style={{ fontSize: "14px" }} className="p-col" >
      {" "}
      {props.labelName + " "}{" "}
    </label>
  </>
);

export function GetStyle(symbolId: string) {
  let style = globalSymbolStyleData.get(symbolId);
  if (style !== undefined) {
    return Object.fromEntries(style);
  }
}

function GetInputNumberStyle(symbolId: string) {
  let style = globalSymbolStyleData.get(symbolId);
  if (style !== undefined) {
    return Object.fromEntries(style);
  } else {
    return defaultInputNumberStyleMap;
  }
}

function GetDropDownStyle(symbolId: string) {
  let style = globalSymbolStyleData.get(symbolId);
  if (style !== undefined) {
    return Object.fromEntries(style);
  } else {
    return defaultDropDownStyleMap;
  }
}

export function GetInputNumber(props: {
  componentId: any;
  symbolId: any;
  symbolValue: any;
  minFractionValue: any;
  minValue: any;
  maxValue: any;
  styleObject : any;
  onChange: (arg0: any) => void;
}) {
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
      onChange={(target) => updateValue(target.value)}
    />
  );
}

export function GetDropDown(props: {
  componentId: any;
  symbolId: any;
  symbolValue: any;
  symbolArray: any;
  styleObject : any;
  onChange: (arg0: any) => void;
}) {
  function updateValue(event: { value: any }) {
    UpdateSymbolValue(props.componentId, props.symbolId, event.value);
    props.onChange(event);
  }
  return (
    <Dropdown
      id={props.symbolId}
      style={props.styleObject}
      value={props.symbolValue}
      options={props.symbolArray}
      onChange={(e) => updateValue(e)}
    />
  );
}

export function GetCheckBox(props: {
  componentId: any;
  symbolId: any;
  symbolValue: string;
  styleObject : any;
  onChange: (arg0: any) => void;
}) {
  function updateValue(checked: boolean) {
    UpdateSymbolValue(props.componentId, props.symbolId, checked);
    props.onChange(checked);
  }
  return (
    <Checkbox
      id={props.symbolId}
      inputId="binary"
      style={props.styleObject}
      checked={convertToBoolean(props.symbolValue)}
      onChange={(e) => updateValue(e.checked)}
    />
  );
}

export function GetButton(props: {
  buttonId: string;
  buttonDisplayText: string;
  onChange: (arg0: any) => void;
}) {
  return (
    <Button
      type="button"
      className="p-button-raised p-button-rounded"
      label={props.buttonDisplayText}
      tooltip="View Configurations"
      tooltipOptions={{ position: "bottom" }}
      style={GetStyle(props.buttonId)}
      onClick={(e) => props.onChange(e)}
    />
  );
}

export const GetLabelWithCustomDisplay: React.FC<CustomLabel> = (
  props
): JSX.Element => (
  <>
    <label
      style={props.labelStyle}
      id={props.labelId}
    >
      {props.labelDisplayText}
    </label>
  </>
);

export const GetLabelWithCustomDisplayWithTooltip: React.FC<CustomLabelWithTooltip> = (
  props
): JSX.Element => (
  <>
    <label
      style={props.labelStyle}
      id={props.labelId}
      title = {props.labelTooltip}
    >
      {props.labelDisplayText}
    </label>
  </>
);


let requiredStyles = ["position", "top", "left", "width", "height"];

export function StoreSymbolStyle(symbolId: string, styleMap: Map<any, any>) {
  let map = new Map<string, string>();
  styleMap.forEach((value, key) => {
    if (key === symbolId) {
      for (let k in value) {
        // if (requiredStyles.includes(k)) {
        if (k === "top" || k === "left") {
          let v = value[k];
          v = v.replace("px", "");
          v = Number(v) + 10;
          if (k === "top") {
            v = Number(v) + Number(toolBarHeight.replace("px", ""));
          }
          map.set(k, v + "px");
        } else if (k === "width" || k === "height") {
          let v = value[k];
          map.set(k, v);
        } else {
          map.set(k, value[k]);
        }
      }
      // }
    }
  });
  globalSymbolStyleData.set(symbolId, map);
}
