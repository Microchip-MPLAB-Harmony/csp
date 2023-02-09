"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.StoreSymbolStyle = exports.GetStyle = exports.GetUIComponentWithOutLabel = exports.GetUIComponentWithLabel = exports.GetMinFractionValueBasedSymbolType = exports.SymbolType = exports.defaultDropDownStyleMap = exports.defaultInputNumberStyleMap = exports.globalSymbolSStateData = exports.globalSymbolStyleData = void 0;
const SymbolAccess_1 = require("@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess");
const CustomConsole_1 = require("@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole");
const react_1 = __importDefault(require("react"));
const CheckBox_1 = __importDefault(require("@mplab_harmony/harmony-plugin-ui/build/components/CheckBox"));
const DropDown_1 = __importDefault(require("@mplab_harmony/harmony-plugin-ui/build/components/DropDown"));
const InputNumber_1 = __importDefault(require("@mplab_harmony/harmony-plugin-ui/build/components/InputNumber"));
const Label_1 = require("@mplab_harmony/harmony-plugin-ui/build/components/Label");
exports.globalSymbolStyleData = new Map();
exports.globalSymbolSStateData = new Map();
exports.defaultInputNumberStyleMap = new Map();
exports.defaultDropDownStyleMap = new Map();
var SymbolType;
(function (SymbolType) {
    SymbolType[SymbolType["DropDown"] = 0] = "DropDown";
    SymbolType[SymbolType["InputNumber"] = 1] = "InputNumber";
    SymbolType[SymbolType["CheckBox"] = 2] = "CheckBox";
    SymbolType[SymbolType["String"] = 3] = "String";
})(SymbolType = exports.SymbolType || (exports.SymbolType = {}));
function Component(props) {
    let component;
    let value = (0, SymbolAccess_1.GetSymbolValue)(props.componentId, props.symbolId);
    if (value === null) {
        (0, CustomConsole_1.error)('Missing_Symbol: ' + props.symbolId);
        return null;
    }
    let symbolVisibleStatus = (0, SymbolAccess_1.GetSymbolVisibleStatus)(props.componentId, props.symbolId) === true
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
            component = (react_1.default.createElement(DropDown_1.default, { componentId: props.componentId, symbolId: props.symbolId, symbolListeners: props.symbolListeners, symbolValue: value, symbolArray: (0, SymbolAccess_1.GetSymbolArray)(props.componentId, props.symbolId), styleObject: GetDropDownStyle(props.symbolId), className: null, readOnly: (0, SymbolAccess_1.GetSymbolReadOnlyStatus)(props.componentId, props.symbolId), visible: symbolVisibleStatus, onChange: (target) => props.onChange(target.target) }));
            break;
        case SymbolType.InputNumber:
            component = (react_1.default.createElement(InputNumber_1.default, { componentId: props.componentId, symbolId: props.symbolId, symbolValue: value, symbolListeners: props.symbolListeners, minFractionValue: GetMinFractionValueBasedSymbolType(props.componentId, props.symbolId), minValue: (0, SymbolAccess_1.GetSymbolMinValue)(props.componentId, props.symbolId), maxValue: (0, SymbolAccess_1.GetSymbolMaxValue)(props.componentId, props.symbolId), styleObject: GetInputNumberStyle(props.symbolId), className: null, readOnly: (0, SymbolAccess_1.GetSymbolReadOnlyStatus)(props.componentId, props.symbolId), onChange: (target) => props.onChange(target.target), visible: symbolVisibleStatus }));
            break;
        case SymbolType.CheckBox:
            component = (react_1.default.createElement(CheckBox_1.default, { componentId: props.componentId, symbolId: props.symbolId, symbolListeners: props.symbolListeners, symbolValue: value, styleObject: GetStyle(props.symbolId), className: null, readOnly: (0, SymbolAccess_1.GetSymbolReadOnlyStatus)(props.componentId, props.symbolId), visible: symbolVisibleStatus, onChange: (target) => props.onChange(target.target) }));
            break;
        case SymbolType.String:
            component = (react_1.default.createElement("div", { className: "p-text-italic" },
                react_1.default.createElement(Label_1.DisplayLabel, { labelName: value })));
            break;
        default:
            (0, CustomConsole_1.error)('Invalid SymbolType.');
    }
    return component;
}
function ComponentWithLabel(props) {
    let component = Component(props);
    if (component === null) {
        return null;
    }
    return (react_1.default.createElement("div", { className: "grid" },
        react_1.default.createElement("div", { className: "col" },
            react_1.default.createElement(Label_1.DisplayLabel, { labelName: (0, SymbolAccess_1.GetSymbolLabelName)(props.componentId, props.symbolId) }),
            ' '),
        react_1.default.createElement("div", { className: "col-fixed", style: { width: 510 } }, component)));
}
function ComponentWithOutLabel(props) {
    return (react_1.default.createElement("div", null,
        react_1.default.createElement(Component, { componentId: props.componentId, symbolId: props.symbolId, symbolListeners: props.symbolListeners, onChange: props.onChange })));
}
function GetMinFractionValueBasedSymbolType(componentId, symbolID) {
    let typeofSymbol = (0, SymbolAccess_1.GetSymbolType)(componentId, symbolID);
    if (typeofSymbol === 'Float') {
        return 1;
    }
    return 0;
}
exports.GetMinFractionValueBasedSymbolType = GetMinFractionValueBasedSymbolType;
function GetComponentType(props) {
    let typeofSymbol = (0, SymbolAccess_1.GetSymbolType)(props.componentId, props.symbolID);
    let type;
    switch (typeofSymbol) {
        case 'Boolean':
            type = SymbolType.CheckBox;
            break;
        case 'Integer':
        case 'Long':
        case 'Hex':
        case 'Float':
            type = SymbolType.InputNumber;
            break;
        case 'KeyValueSet':
        case 'ComboSymbol':
        case 'Combo':
            type = SymbolType.DropDown;
            break;
        case 'String':
            type = SymbolType.String;
            break;
        default:
            (0, CustomConsole_1.error)('Invalid SymbolType ' + props.symbolID);
    }
    return type;
}
function GetUIComponentWithLabel(props) {
    return (react_1.default.createElement("div", null,
        react_1.default.createElement(ComponentWithLabel, { componentId: props.componentId, symbolId: props.symbolId, symbolListeners: props.symbolListeners, onChange: props.onChange })));
}
exports.GetUIComponentWithLabel = GetUIComponentWithLabel;
function GetUIComponentWithOutLabel(props) {
    return (react_1.default.createElement("div", null,
        react_1.default.createElement(ComponentWithOutLabel, { componentId: props.componentId, symbolId: props.symbolId, symbolListeners: props.symbolListeners, onChange: props.onChange })));
}
exports.GetUIComponentWithOutLabel = GetUIComponentWithOutLabel;
function GetStyle(symbolId) {
    let style = exports.globalSymbolStyleData.get(symbolId);
    if (style !== undefined) {
        return Object.fromEntries(style);
    }
}
exports.GetStyle = GetStyle;
function GetInputNumberStyle(symbolId) {
    let style = exports.globalSymbolStyleData.get(symbolId);
    if (style !== undefined) {
        return Object.fromEntries(style);
    }
    else {
        return Object.fromEntries(exports.defaultInputNumberStyleMap);
    }
}
function GetDropDownStyle(symbolId) {
    let style = exports.globalSymbolStyleData.get(symbolId);
    if (style !== undefined) {
        return Object.fromEntries(style);
    }
    else {
        return Object.fromEntries(exports.defaultDropDownStyleMap);
    }
}
let requiredStyles = ['position', 'top', 'left', 'width', 'height'];
function StoreSymbolStyle(toolBarHeight, symbolId, styleMap) {
    let map = new Map();
    styleMap.forEach((value, key) => {
        if (key === symbolId) {
            for (let k in value) {
                if (k === 'top' || k === 'left') {
                    let v = value[k];
                    v = v.replace('px', '');
                    v = Number(v) + 10;
                    if (k === 'top') {
                        v = Number(v) + Number(toolBarHeight.replace('px', ''));
                    }
                    map.set(k, v + 'px');
                }
                else if (k === 'width' || k === 'height') {
                    let v = value[k];
                    map.set(k, v);
                }
                else {
                    map.set(k, value[k]);
                }
            }
        }
    });
    exports.globalSymbolStyleData.set(symbolId, map);
}
exports.StoreSymbolStyle = StoreSymbolStyle;
class Components {
}
exports.default = Components;
