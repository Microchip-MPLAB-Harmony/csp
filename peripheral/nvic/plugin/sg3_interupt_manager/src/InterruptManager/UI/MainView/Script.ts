import { GetSymbolValue } from "../../Common/SymbolAccess";
import { component_id } from "./MainBlock";

export let RowAndVectorInterruptMap = new Map();
let totalRowLength = 0;

export function UpdateRowAndVectorInterruptMap() {
  let totalVectorLines = GetSymbolValue(component_id, "NVIC_NUM_VECTORS");
  let vectorNum, interruptNumbers ;
  for (let i = 0; i < totalVectorLines; i++) {
    vectorNum = GetSymbolValue(component_id, "NVIC_VECTOR_NUM_" + i);
    interruptNumbers = GetSymbolValue(component_id, "NVIC_NUM_INTERRUPTS_" + i);
    for (let j = 0; j < interruptNumbers; j++) {
      RowAndVectorInterruptMap.set(totalRowLength, vectorNum + "_" + j);
      totalRowLength++;
    }
    if (interruptNumbers === 0) {
      alert("For vector number: " + vectorNum + " , Interrupt length is zero.");
    }
  }
}