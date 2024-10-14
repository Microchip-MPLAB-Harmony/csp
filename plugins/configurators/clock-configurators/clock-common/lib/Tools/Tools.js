"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.GetClockDisplayFreqValue = exports.GetDivValue = exports.removeDuplicates = void 0;
const removeDuplicates = (symbolsArray) => {
    return symbolsArray;
};
exports.removeDuplicates = removeDuplicates;
const GetDivValue = (text) => {
    try {
        const divValue = text.replace('DIV', '');
        return divValue;
    }
    catch (err) {
    }
};
exports.GetDivValue = GetDivValue;
const GetClockDisplayFreqValue = (value) => {
    let newfreqValue = '';
    if (value === 0) {
        newfreqValue = value.toString() + ' Hz';
        return newfreqValue;
    }
    let freqValue = value / 1000000;
    if (!Number.isInteger(freqValue)) {
        if (freqValue < 1) {
            freqValue = value / 1000;
            newfreqValue = freqValue.toFixed(3) + ' KHz';
        }
        else {
            newfreqValue = freqValue.toFixed(3) + ' MHz';
        }
    }
    else {
        newfreqValue = freqValue.toString() + ' MHz';
    }
    return newfreqValue;
};
exports.GetClockDisplayFreqValue = GetClockDisplayFreqValue;
