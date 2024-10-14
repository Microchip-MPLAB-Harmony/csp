const removeDuplicates = (symbolsArray: string[]) => {
  // return symbolsArray.filter((item, index) => symbolsArray.indexOf(item) === index);
  return symbolsArray;
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
      newfreqValue = freqValue.toFixed(3) + ' KHz';
    } else {
      newfreqValue = freqValue.toFixed(3) + ' MHz';
    }
  } else {
    newfreqValue = freqValue.toString() + ' MHz';
  }
  return newfreqValue;
};
export { removeDuplicates, GetDivValue, GetClockDisplayFreqValue };
