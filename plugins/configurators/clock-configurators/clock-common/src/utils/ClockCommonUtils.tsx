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
import { InputNumber as PrimeInputNumber } from 'primereact/inputnumber';
import { Checkbox as PrimeCheckbox } from 'primereact/checkbox';
import {
  GetMinFractionValueBasedSymbolType,
  GetStyle
} from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

import {
  GetSymbolArray,
  GetSymbolMaxValue,
  GetSymbolMinValue,
  GetSymbolReadOnlyStatus,
  GetSymbolValue,
  GetSymbolVisibleStatus
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import InputNumber from '@mplab_harmony/harmony-plugin-ui/build/components/InputNumber';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import { error } from '@mplab_harmony/harmony-plugin-core-service';
import React from 'react';

export function AddCombobox(component_id: string, symbolId: string, styleId: string) {
  function ValueChange(_onChangeData: Map<any, any>) {
    // do nothing
  }
  try {
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbolId}
          onChange={ValueChange}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          symbolListeners={[symbolId]}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          visible={GetSymbolVisibleStatus(component_id, symbolId)}
        />
      </div>
    );
  } catch (err) {
    error(err);
  }
}

export function AddCheckBox(component_id: string, symbolId: string, styleId: string) {
  function ValueChange(_onChangeData: Map<any, any>) {
    // do nothing
  }
  try {
    return (
      <div>
        <CheckBox
          componentId={component_id}
          symbolId={symbolId}
          onChange={ValueChange}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          symbolListeners={[symbolId]}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          visible={GetSymbolVisibleStatus(component_id, symbolId)}
        />
      </div>
    );
  } catch (err) {
    error(err);
  }
}

export function AddInputNumber(component_id: string, symbolId: string, styleId: string) {
  function ValueChange(_onChangeData: Map<any, any>) {
    // do nothing
  }
  try {
    return (
      <div>
        <InputNumber
          componentId={component_id}
          symbolId={symbolId}
          onChange={ValueChange}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          minFractionValue={GetMinFractionValueBasedSymbolType(component_id, symbolId)}
          minValue={GetSymbolMinValue(component_id, symbolId)}
          maxValue={GetSymbolMaxValue(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          symbolListeners={[symbolId]}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          visible={GetSymbolVisibleStatus(component_id, symbolId)}
        />
      </div>
    );
  } catch (err) {
    error(err);
  }
}

export function AddDummyInputNumber(styleId: string) {
  return (
    <div>
      <PrimeInputNumber
        value={0}
        disabled
        style={GetStyle(styleId)}
      />
    </div>
  );
}

export function AddDummyCheckBox(styleId: string) {
  return (
    <div>
      <PrimeCheckbox
        value={false}
        disabled
        style={GetStyle(styleId)}
      />
    </div>
  );
}
