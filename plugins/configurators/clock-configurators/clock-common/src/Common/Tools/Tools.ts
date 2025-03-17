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
  let newfreqValue;
  let freqValue = value / 1000000;

  function formatNumber(num: number, decimals: number) {
    return num.toFixed(decimals).replace(/\.?0+$/, '');
  }

  if (freqValue < 1) {
    freqValue = value / 1000;
    if (freqValue < 1) {
      newfreqValue = formatNumber(value, 3) + ' Hz';
    } else {
      newfreqValue = formatNumber(freqValue, 3) + ' kHz';
    }
  } else {
    newfreqValue = formatNumber(freqValue, 6) + ' MHz';
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
