import {
  GetStyle,
  globalSymbolStyleData,
  StoreSymbolStyle
} from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

export class SVGSymbolStyleService {
  private readonly a: number = 10;
  private readonly symbolsArray: string[] = [];
  private readonly labelsArray: string[] = [];

  constructor(symbolStylesJSON: any, dynamicSymbolsIgnoreList: string[]) {}

  ReadJSONData(symbolStylesJSON: any, dynamicSymbolsIgnoreList: string[]) {
    const symbolsStyle = new Map<any, any>();
    this.symbolsArray.length = 0;
    this.labelsArray.length = 0;
    globalSymbolStyleData.clear();
    for (let prop in symbolStylesJSON) {
      const settings = symbolStylesJSON[prop];
      if (prop.startsWith('sym_')) {
        prop = prop.replace('sym_', '');
        if (!dynamicSymbolsIgnoreList.includes(prop)) {
          this.symbolsArray.push(prop);
        }
      } else if (prop.startsWith('label_sym_')) {
        prop = prop.replace('label_sym_', '');
        if (!dynamicSymbolsIgnoreList.includes(prop)) {
          this.labelsArray.push(prop);
        }
      }
      for (const temp in settings) {
        symbolsStyle.set(prop, settings[temp]);
      }
      StoreSymbolStyle(toolBarHeight, prop, symbolsStyle);
    }
  }

  flushStore(): void {}

  get abcd(): number {
    return this.a;
  }
}
