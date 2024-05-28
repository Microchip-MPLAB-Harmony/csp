"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.GetDivValue = exports.removeDuplicates = void 0;
function removeDuplicates(symbolsArray) {
    return symbolsArray.filter((item, index) => symbolsArray.indexOf(item) === index);
}
exports.removeDuplicates = removeDuplicates;
function GetDivValue(text) {
    try {
        const divValue = text.replace('DIV', '');
        return divValue;
    }
    catch (err) {
    }
}
exports.GetDivValue = GetDivValue;
