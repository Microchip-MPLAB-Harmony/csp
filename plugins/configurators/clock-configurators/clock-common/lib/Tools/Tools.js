"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.getSymbolValue = exports.GetClockDisplayFreqValue = exports.GetDivValue = exports.removeDuplicates = void 0;
const harmony_plugin_client_lib_1 = require("@mplab_harmony/harmony-plugin-client-lib");
const removeDuplicates = (symbolsArray) => {
    return symbolsArray.filter((item, index) => symbolsArray.indexOf(item) === index);
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
    let newfreqValue;
    let freqValue = value / 1000000;
    function formatNumber(num, decimals) {
        return num.toFixed(decimals).replace(/\.?0+$/, '');
    }
    if (freqValue < 1) {
        freqValue = value / 1000;
        if (freqValue < 1) {
            newfreqValue = formatNumber(value, 3) + ' Hz';
        }
        else {
            newfreqValue = formatNumber(freqValue, 3) + ' kHz';
        }
    }
    else {
        newfreqValue = formatNumber(freqValue, 6) + ' MHz';
    }
    return newfreqValue;
};
exports.GetClockDisplayFreqValue = GetClockDisplayFreqValue;
const getSymbolValue = (componentId, symbolId) => __awaiter(void 0, void 0, void 0, function* () {
    const symbols = (yield harmony_plugin_client_lib_1.symbolUtilApi.getSymbols(componentId, [symbolId]));
    for (const symbol of symbols) {
        return symbol.value;
    }
});
exports.getSymbolValue = getSymbolValue;
