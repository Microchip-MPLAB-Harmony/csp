import {
  GetSymbolArray,
  GetSymbolValue,
  GetSymbolLabelName,
  GetSymbolMinValue,
  GetSymbolMaxValue,
  GetSymbolType,
  GetSymbolVisibleStatus,
} from "../SymbolAccess";
import { toolBarHeight } from "../../UI/MainView/MainBlock";
import { GetSymbolEnableStatus } from "../SymbolAccess";
import GetCheckBox from "./CheckBox";
import GetDropDown from "./DropDown";
import GetInputNumber from "./InputNumber";
import { DisplayLabel } from "./Label";

export let globalSymbolStyleData = new Map<any, Map<string, string>>();
export let globalSymbolSStateData = new Map<any, any>();
export let defaultInputNumberStyleMap = new Map<string, string>();
export let defaultDropDownStyleMap = new Map<string, string>();

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
          editable={GetSymbolEnableStatus(props.componentId, props.symbolId)}
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
          editable={GetSymbolEnableStatus(props.componentId, props.symbolId)}
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
          editable={GetSymbolEnableStatus(props.componentId, props.symbolId)}
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

export function GetMinFractionValueBasedSymbolType(
  componentId: any,
  symbolID: any
) {
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
    return Object.fromEntries(defaultInputNumberStyleMap);
  }
}

function GetDropDownStyle(symbolId: string) {
  let style = globalSymbolStyleData.get(symbolId);
  if (style !== undefined) {
    return Object.fromEntries(style);
  } else {
    return Object.fromEntries(defaultDropDownStyleMap);
  }
}

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

export function symbolListnerSymbolChanged(symbolid :string){
  alert(symbolid + " changed.......................")
}

