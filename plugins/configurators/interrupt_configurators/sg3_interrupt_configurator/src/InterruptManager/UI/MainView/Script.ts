/*
 * Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
 *
 * Subject to your compliance with these terms, you may use Microchip software
 * and any derivatives exclusively with Microchip products. It is your
 * responsibility to comply with third party license terms applicable to your
 * use of third party software (including open source software) that may
 * accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
 * EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
 * WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
 * PARTICULAR PURPOSE.
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
 * INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
 * WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
 * BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
 * FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
 * ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
 * THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 */
import { error } from '@mplab_harmony/harmony-plugin-core-service';
import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { component_id } from './MainBlock';

export let RowAndVectorInterruptMap = new Map();
let totalRowLength = 0;

export function UpdateRowAndVectorInterruptMap() {
  let totalVectorLines = GetSymbolValue(component_id, 'NVIC_NUM_VECTORS');
  let vectorNum, interruptNumbers;
  for (let i = 0; i < totalVectorLines; i++) {
    vectorNum = GetSymbolValue(component_id, 'NVIC_VECTOR_NUM_' + i);
    interruptNumbers = GetSymbolValue(component_id, 'NVIC_NUM_INTERRUPTS_' + i);
    for (let j = 0; j < interruptNumbers; j++) {
      RowAndVectorInterruptMap.set(totalRowLength, vectorNum + '_' + j);
      totalRowLength++;
    }
    if (interruptNumbers === 0) {
      error('For vector number: ' + vectorNum + ' , Interrupt length is zero.');
    }
  }
}
