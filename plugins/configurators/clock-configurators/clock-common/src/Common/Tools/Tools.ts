export function removeDuplicates(symbolsArray: string[]) {
  return symbolsArray.filter((item, index) => symbolsArray.indexOf(item) === index);
}

export function GetDivValue(text: any) {
  try {
    const divValue = text.replace('DIV', '');
    return divValue;
  } catch (err) {
    /* empty */
  }
}
