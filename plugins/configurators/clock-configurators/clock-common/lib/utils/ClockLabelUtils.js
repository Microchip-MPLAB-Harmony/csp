"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AddPrefixDivSymbolLabel = exports.AddMinMaxSymboLabelWithSuffix = exports.AddSymboLabelWithSuffixWithBold = exports.AddSymboLabelWithSuffix = exports.AddPlainLabelWithBold = exports.AddPlainLabel = exports.GetBoldStyledObject = exports.GetColeredStyledObject = void 0;
const SymbolAccess_1 = require("@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess");
const Components_1 = require("@mplab_harmony/harmony-plugin-ui/build/components/Components");
const StateLabel_1 = __importDefault(require("@mplab_harmony/harmony-plugin-ui/build/components/StateLabel"));
const ComponentStateChangeUtils_1 = require("@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils");
const react_1 = __importDefault(require("react"));
const defaultColor = 'black';
function GetColeredStyledObject(labelId, changeColorStatus, changeColor) {
    try {
        const style = Components_1.globalSymbolStyleData.get(labelId);
        if (style !== undefined) {
            if (changeColorStatus === true) {
                style.set('color', changeColor);
            }
            else {
                style.set('color', defaultColor);
            }
        }
        return Object.fromEntries(style);
    }
    catch (err) {
    }
}
exports.GetColeredStyledObject = GetColeredStyledObject;
function GetBoldStyledObject(labelId, boldStatus) {
    try {
        const style = Components_1.globalSymbolStyleData.get(labelId);
        if (style !== undefined) {
            if (boldStatus === true) {
                style.set('font-weight', 'bold');
            }
            else {
                style.set('font-weight', 'normal');
            }
        }
        return Object.fromEntries(style);
    }
    catch (err) {
    }
}
exports.GetBoldStyledObject = GetBoldStyledObject;
function AddPlainLabel(labelId, text) {
    try {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(StateLabel_1.default, { labelId: labelId, labelDisplayText: text, labelStyle: (0, Components_1.GetStyle)(labelId) })));
    }
    catch (err) {
    }
}
exports.AddPlainLabel = AddPlainLabel;
function AddPlainLabelWithBold(labelId, text, boldStatus) {
    try {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(StateLabel_1.default, { labelId: labelId, labelDisplayText: text, labelStyle: GetBoldStyledObject(labelId, boldStatus) })));
    }
    catch (err) {
    }
}
exports.AddPlainLabelWithBold = AddPlainLabelWithBold;
function AddSymboLabelWithSuffix(labelId, component_id, symbolId, suffix) {
    try {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(StateLabel_1.default, { labelId: labelId, labelDisplayText: (0, SymbolAccess_1.GetSymbolValue)(component_id, symbolId), labelSuffixText: suffix, labelStyle: (0, Components_1.GetStyle)(labelId), symbolListeners: [symbolId] })));
    }
    catch (err) {
    }
}
exports.AddSymboLabelWithSuffix = AddSymboLabelWithSuffix;
function AddSymboLabelWithSuffixWithBold(labelId, component_id, symbolId, suffix, boldStatus) {
    try {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(StateLabel_1.default, { labelId: labelId, labelDisplayText: (0, SymbolAccess_1.GetSymbolValue)(component_id, symbolId), labelSuffixText: suffix, labelStyle: GetBoldStyledObject(labelId, boldStatus), symbolListeners: [symbolId] })));
    }
    catch (err) {
    }
}
exports.AddSymboLabelWithSuffixWithBold = AddSymboLabelWithSuffixWithBold;
function AddMinMaxSymboLabelWithSuffix(labelId, component_id, symbolId, suffix, minValue, maxValue, changeColor, labelTooltip) {
    function ColorChangeStatus(minValue, maxValue, newValue) {
        const status = Number(newValue) >= Number(minValue) && Number(newValue) <= Number(maxValue) ? true : false;
        return !status;
    }
    function customLabelConfigOnSymbolChange(symbolId, currentSymbolValue) {
        (0, ComponentStateChangeUtils_1.ChangeCustomLabelComponentState)(symbolId, currentSymbolValue, GetColeredStyledObject(labelId, ColorChangeStatus(minValue, maxValue, currentSymbolValue), changeColor), true, null);
    }
    try {
        const symbolValue = (0, SymbolAccess_1.GetSymbolValue)(component_id, symbolId);
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(StateLabel_1.default, { labelId: labelId, labelDisplayText: symbolValue, labelSuffixText: suffix, labelStyle: GetColeredStyledObject(labelId, ColorChangeStatus(minValue, maxValue, symbolValue), changeColor), symbolListeners: [symbolId], labelTooltip: labelTooltip, customLabelConfigOnSymbolChange: customLabelConfigOnSymbolChange })));
    }
    catch (err) {
    }
}
exports.AddMinMaxSymboLabelWithSuffix = AddMinMaxSymboLabelWithSuffix;
function AddPrefixDivSymbolLabel(id, component_id, symbolId, InputFormat) {
    function customLabelConfigOnSymbolChange(symbolId, value) {
        (0, ComponentStateChangeUtils_1.ChangeCustomLabelComponentState)(symbolId, InputFormat(value), null, null, null);
    }
    try {
        return (react_1.default.createElement("div", null,
            react_1.default.createElement(StateLabel_1.default, { labelId: id, labelDisplayText: InputFormat((0, SymbolAccess_1.GetSymbolValue)(component_id, symbolId)), labelStyle: (0, Components_1.GetStyle)(id), symbolListeners: [symbolId], customLabelConfigOnSymbolChange: customLabelConfigOnSymbolChange })));
    }
    catch (err) {
    }
}
exports.AddPrefixDivSymbolLabel = AddPrefixDivSymbolLabel;
