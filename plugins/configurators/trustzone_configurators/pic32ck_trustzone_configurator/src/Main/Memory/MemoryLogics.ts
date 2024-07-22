export function SetMinMaxSliderCallableSlider(
  nParentSliderValue: any,
  nGranularityFactor: any,
  symbolArrayLength: any,
  setMinMaxSlider: (arg0: any, arg1: any, arg2: any) => void
) {
  let nCallableArrayLength = nParentSliderValue * nGranularityFactor;
  let nMaxIndex = symbolArrayLength - 1;
  let isCalalbleMore = false;
  if (nCallableArrayLength > nMaxIndex) {
    nCallableArrayLength = nMaxIndex;
    isCalalbleMore = true;
  }
  if (nParentSliderValue !== 0) {
    if (isCalalbleMore) {
      nParentSliderValue = nParentSliderValue + nCallableArrayLength;
    } else {
      nParentSliderValue = nCallableArrayLength;
    }
  }
  setMinMaxSlider(0, nParentSliderValue, nCallableArrayLength);
}

export const ByteToHex = (byte: any) => {
  byte = Number(byte);
  let hexString = byte.toString(16);
  return '0x' + hexString;
};

export const RemoveBytesStr = (byte: any) => {
  byte = byte.replace(' Bytes', '');
  return Number(byte);
};

export function SetSliderValueUpperValueSymbolType(sliderValue: any, sliderMaxValue: any) {
  if (sliderValue == null) {
    return 0;
  } else {
    return sliderMaxValue - sliderValue;
  }
}
export function SetSliderValueLowerValueSymbolType(value: any, sliderMaxValue: any) {
  if (value == null) {
    return sliderMaxValue;
  } else {
    return value;
  }
}

export function GetValidSilderSymbolValue(value: number, sliderMax: any, nSliderRestricRange: any) {
  if (value == null) {
    return null;
  }
  if (nSliderRestricRange < value) {
    value = sliderMax;
    return value;
  }
  return value;
}
