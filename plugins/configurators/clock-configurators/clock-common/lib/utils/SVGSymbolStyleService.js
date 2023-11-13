"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.SVGSymbolStyleService = void 0;
const Components_1 = require("@mplab_harmony/harmony-plugin-ui/build/components/Components");
class SVGSymbolStyleService {
    constructor(symbolStylesJSON, dynamicSymbolsIgnoreList) {
        this.a = 10;
        this.symbolsArray = [];
        this.labelsArray = [];
    }
    ReadJSONData(symbolStylesJSON, dynamicSymbolsIgnoreList) {
        const symbolsStyle = new Map();
        this.symbolsArray.length = 0;
        this.labelsArray.length = 0;
        Components_1.globalSymbolStyleData.clear();
        for (let prop in symbolStylesJSON) {
            const settings = symbolStylesJSON[prop];
            if (prop.startsWith('sym_')) {
                prop = prop.replace('sym_', '');
                if (!dynamicSymbolsIgnoreList.includes(prop)) {
                    this.symbolsArray.push(prop);
                }
            }
            else if (prop.startsWith('label_sym_')) {
                prop = prop.replace('label_sym_', '');
                if (!dynamicSymbolsIgnoreList.includes(prop)) {
                    this.labelsArray.push(prop);
                }
            }
            for (const temp in settings) {
                symbolsStyle.set(prop, settings[temp]);
            }
            (0, Components_1.StoreSymbolStyle)(toolBarHeight, prop, symbolsStyle);
        }
    }
    flushStore() { }
    get abcd() {
        return this.a;
    }
}
exports.SVGSymbolStyleService = SVGSymbolStyleService;
