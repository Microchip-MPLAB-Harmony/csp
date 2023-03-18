"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AddDummyCheckBox = exports.AddDummyInputNumber = exports.AddInputNumber = exports.AddCheckBox = exports.AddCombobox = void 0;
const inputnumber_1 = require("primereact/inputnumber");
const checkbox_1 = require("primereact/checkbox");
const Components_1 = require("@mplab_harmony/harmony-plugin-ui/build/components/Components");
const SymbolAccess_1 = require("@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess");
const CheckBox_1 = __importDefault(require("@mplab_harmony/harmony-plugin-ui/build/components/CheckBox"));
const InputNumber_1 = __importDefault(require("@mplab_harmony/harmony-plugin-ui/build/components/InputNumber"));
const DropDown_1 = __importDefault(require("@mplab_harmony/harmony-plugin-ui/build/components/DropDown"));
const harmony_plugin_core_service_1 = require("@mplab_harmony/harmony-plugin-core-service");
const react_1 = __importDefault(require("react"));
function AddCombobox(component_id, symbolId, styleId) {
    function ValueChange(_onChangeData) {
    }
    try {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(DropDown_1.default, { componentId: component_id, symbolId: symbolId, onChange: ValueChange, symbolValue: (0, SymbolAccess_1.GetSymbolValue)(component_id, symbolId), symbolArray: (0, SymbolAccess_1.GetSymbolArray)(component_id, symbolId), styleObject: (0, Components_1.GetStyle)(styleId), symbolListeners: [symbolId], readOnly: (0, SymbolAccess_1.GetSymbolReadOnlyStatus)(component_id, symbolId), visible: (0, SymbolAccess_1.GetSymbolVisibleStatus)(component_id, symbolId) })));
    }
    catch (err) {
        (0, harmony_plugin_core_service_1.error)(err);
    }
}
exports.AddCombobox = AddCombobox;
function AddCheckBox(component_id, symbolId, styleId) {
    function ValueChange(_onChangeData) {
    }
    try {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(CheckBox_1.default, { componentId: component_id, symbolId: symbolId, onChange: ValueChange, symbolValue: (0, SymbolAccess_1.GetSymbolValue)(component_id, symbolId), styleObject: (0, Components_1.GetStyle)(styleId), symbolListeners: [symbolId], readOnly: (0, SymbolAccess_1.GetSymbolReadOnlyStatus)(component_id, symbolId), visible: (0, SymbolAccess_1.GetSymbolVisibleStatus)(component_id, symbolId) })));
    }
    catch (err) {
        (0, harmony_plugin_core_service_1.error)(err);
    }
}
exports.AddCheckBox = AddCheckBox;
function AddInputNumber(component_id, symbolId, styleId) {
    function ValueChange(_onChangeData) {
    }
    try {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(InputNumber_1.default, { componentId: component_id, symbolId: symbolId, onChange: ValueChange, symbolValue: (0, SymbolAccess_1.GetSymbolValue)(component_id, symbolId), minFractionValue: (0, Components_1.GetMinFractionValueBasedSymbolType)(component_id, symbolId), minValue: (0, SymbolAccess_1.GetSymbolMinValue)(component_id, symbolId), maxValue: (0, SymbolAccess_1.GetSymbolMaxValue)(component_id, symbolId), styleObject: (0, Components_1.GetStyle)(styleId), symbolListeners: [symbolId], readOnly: (0, SymbolAccess_1.GetSymbolReadOnlyStatus)(component_id, symbolId), visible: (0, SymbolAccess_1.GetSymbolVisibleStatus)(component_id, symbolId) })));
    }
    catch (err) {
        (0, harmony_plugin_core_service_1.error)(err);
    }
}
exports.AddInputNumber = AddInputNumber;
function AddDummyInputNumber(styleId) {
    return (react_1.default.createElement("div", null,
        react_1.default.createElement(inputnumber_1.InputNumber, { value: 0, disabled: true, style: (0, Components_1.GetStyle)(styleId) })));
}
exports.AddDummyInputNumber = AddDummyInputNumber;
function AddDummyCheckBox(styleId) {
    return (react_1.default.createElement("div", null,
        react_1.default.createElement(checkbox_1.Checkbox, { value: false, disabled: true, style: (0, Components_1.GetStyle)(styleId) })));
}
exports.AddDummyCheckBox = AddDummyCheckBox;
