"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getAllSymbolsFromJSON = exports.getRadioButtonFromJSON = exports.getRadioNamesFromJSON = exports.getDynamicLabelsFromJSON = exports.getDynamicSymbolsFromJSON = void 0;
const Tools_1 = require("./Tools");
function getDynamicSymbolsFromJSON(values) {
    return values.filter((e) => e.type === 'dynamic' && e.symbol_id !== undefined);
}
exports.getDynamicSymbolsFromJSON = getDynamicSymbolsFromJSON;
function getConfigurableSymbolsFromJSON(values) {
    return values.filter((e) => e.type !== 'dynamic_label' && e.symbol_id !== undefined);
}
function getDynamicLabelsFromJSON(values) {
    return values.filter((e) => e.type === 'dynamic_label' && e.symbol_id !== undefined);
}
exports.getDynamicLabelsFromJSON = getDynamicLabelsFromJSON;
function getRadioNamesFromJSON(values, radioButtonIdentifactionId) {
    return values.filter((e) => e.type === 'radio_name' && e.symbol_id === radioButtonIdentifactionId);
}
exports.getRadioNamesFromJSON = getRadioNamesFromJSON;
function getRadioButtonFromJSON(values, radioButtonIdentifactionId) {
    return values.filter((e) => e.type === 'radio' && e.symbol_id === radioButtonIdentifactionId);
}
exports.getRadioButtonFromJSON = getRadioButtonFromJSON;
function getAllSymbolsFromJSON(values) {
    let symbolIDs = getConfigurableSymbolsFromJSON(values).map((e) => e.symbol_id);
    symbolIDs = (0, Tools_1.removeDuplicates)(symbolIDs);
    return symbolIDs;
}
exports.getAllSymbolsFromJSON = getAllSymbolsFromJSON;
