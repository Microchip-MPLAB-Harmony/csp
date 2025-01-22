import { ConfigSymbol, symbolUtilApi } from '@mplab_harmony/harmony-plugin-client-lib';

const removeDuplicates = (symbolsArray: string[]) => {
  return symbolsArray.filter((item, index) => symbolsArray.indexOf(item) === index);
};

const GetDivValue = (text: any) => {
  try {
    const divValue = text.replace('DIV', '');
    return divValue;
  } catch (err) {
    /* empty */
  }
};

const GetClockDisplayFreqValue = (value: number) => {
  let newfreqValue = '';
  if (value === 0) {
    newfreqValue = value.toString() + ' Hz';
    return newfreqValue;
  }
  let freqValue = value / 1000000;
  if (!Number.isInteger(freqValue)) {
    if (freqValue < 1) {
      freqValue = value / 1000;
      if (freqValue < 1) {
        newfreqValue = value.toFixed(3) + ' Hz';
      } else {
        newfreqValue = freqValue.toFixed(3) + ' KHz';
      }
    } else {
      newfreqValue = freqValue.toFixed(3) + ' MHz';
    }
  } else {
    newfreqValue = freqValue.toString() + ' MHz';
  }
  return newfreqValue;
};

const getSymbolValue = async (componentId: string, symbolId: string) => {
  const symbols = (await symbolUtilApi.getSymbols(componentId, [symbolId])) as ConfigSymbol<any>[];
  for (const symbol of symbols) {
    return symbol.value;
  }
};
export { removeDuplicates, GetDivValue, GetClockDisplayFreqValue, getSymbolValue };
