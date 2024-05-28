import ControlInterface from './ControlInterface';
import { removeDuplicates } from './Tools';

export function getDynamicSymbolsFromJSON(values: ControlInterface[]) {
  return values.filter((e) => e.type === 'dynamic' && e.symbol_id !== undefined);
}

function getConfigurableSymbolsFromJSON(values: ControlInterface[]) {
  return values.filter((e) => e.type !== 'dynamic_label' && e.symbol_id !== undefined);
}

export function getDynamicLabelsFromJSON(values: ControlInterface[]) {
  return values.filter((e) => e.type === 'dynamic_label' && e.symbol_id !== undefined);
}

export function getRadioNamesFromJSON(
  values: ControlInterface[],
  radioButtonIdentifactionId: string
) {
  return values.filter(
    (e) => e.type === 'radio_name' && e.symbol_id === radioButtonIdentifactionId
  );
}

export function getRadioButtonFromJSON(
  values: ControlInterface[],
  radioButtonIdentifactionId: string
) {
  return values.filter((e) => e.type === 'radio' && e.symbol_id === radioButtonIdentifactionId);
}

export function getAllSymbolsFromJSON(values: ControlInterface[]) {
  let symbolIDs = getConfigurableSymbolsFromJSON(values).map((e) => e.symbol_id) as string[];
  symbolIDs = removeDuplicates(symbolIDs);
  return symbolIDs;
}
