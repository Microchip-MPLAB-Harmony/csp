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
import { GetMinFractionValueBasedSymbolType } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';

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

export const AddCombobox = (props: {
  component_id: string;
  symbolId: string;
  className: string;
  styleObj?: any;
}) => {
  function ValueChange(_onChangeData: Map<any, any>) {
    // do nothing
  }
  try {
    return (
      <div>
        <DropDown
          componentId={props.component_id}
          symbolId={props.symbolId}
          onChange={ValueChange}
          symbolValue={GetSymbolValue(props.component_id, props.symbolId)}
          symbolArray={GetSymbolArray(props.component_id, props.symbolId)}
          styleObject={props.styleObj}
          className={props.className}
          symbolListeners={[props.symbolId]}
          readOnly={GetSymbolReadOnlyStatus(props.component_id, props.symbolId)}
          visible={GetSymbolVisibleStatus(props.component_id, props.symbolId)}
        />
      </div>
    );
  } catch (err) {
    error(err);
    return <div></div>;
  }
};

export const AddCheckBox = (props: {
  component_id: string;
  symbolId: string;
  className: string;
  styleObj?: any;
}) => {
  function ValueChange(_onChangeData: Map<any, any>) {
    // do nothing
  }
  try {
    return (
      <div>
        <CheckBox
          componentId={props.component_id}
          symbolId={props.symbolId}
          onChange={ValueChange}
          symbolValue={GetSymbolValue(props.component_id, props.symbolId)}
          styleObject={props.styleObj}
          symbolListeners={[props.symbolId]}
          readOnly={GetSymbolReadOnlyStatus(props.component_id, props.symbolId)}
          visible={GetSymbolVisibleStatus(props.component_id, props.symbolId)}
          className={props.className}
        />
      </div>
    );
  } catch (err) {
    error(err);
    return <div></div>;
  }
};

export function AddInputNumber(props: {
  component_id: string;
  symbolId: string;
  className: string;
  styleObj?: any;
}) {
  function ValueChange(_onChangeData: Map<any, any>) {
    // do nothing
  }
  try {
    return (
      <div>
        <InputNumber
          componentId={props.component_id}
          symbolId={props.symbolId}
          onChange={ValueChange}
          className={props.className}
          symbolValue={GetSymbolValue(props.component_id, props.symbolId)}
          minFractionValue={GetMinFractionValueBasedSymbolType(props.component_id, props.symbolId)}
          minValue={GetSymbolMinValue(props.component_id, props.symbolId)}
          maxValue={GetSymbolMaxValue(props.component_id, props.symbolId)}
          styleObject={props.styleObj}
          symbolListeners={[props.symbolId]}
          readOnly={GetSymbolReadOnlyStatus(props.component_id, props.symbolId)}
          visible={GetSymbolVisibleStatus(props.component_id, props.symbolId)}
        />
      </div>
    );
  } catch (err) {
    error(err);
    return <div></div>;
  }
}

export function AddDummyInputNumber(props: { className: string; styleId?: any }) {
  return (
    <div>
      <PrimeInputNumber
        value={0}
        disabled
        style={props.styleId}
        className={props.className}
      />
    </div>
  );
}

export function AddDummyCheckBox(props: { className: string; styleId?: any }) {
  return (
    <div>
      <PrimeCheckbox
        value={false}
        disabled
        style={props.styleId}
        className={props.className}
      />
    </div>
  );
}
