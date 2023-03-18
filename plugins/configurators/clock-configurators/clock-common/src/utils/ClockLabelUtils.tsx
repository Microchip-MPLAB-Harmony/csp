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

import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import {
  GetStyle,
  globalSymbolStyleData
} from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import StateLabel from '@mplab_harmony/harmony-plugin-ui/build/components/StateLabel';
import { ChangeCustomLabelComponentState } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';
import React from 'react';
const defaultColor = 'black';

export function GetColeredStyledObject(
  labelId: string,
  changeColorStatus: boolean,
  changeColor: string
) {
  try {
    const style: any = globalSymbolStyleData.get(labelId);
    if (style !== undefined) {
      if (changeColorStatus === true) {
        style.set('color', changeColor);
      } else {
        style.set('color', defaultColor);
      }
    }
    return Object.fromEntries(style);
  } catch (err) {
    /* empty */
  }
}

export function GetBoldStyledObject(labelId: any, boldStatus: boolean) {
  try {
    const style: any = globalSymbolStyleData.get(labelId);
    if (style !== undefined) {
      if (boldStatus === true) {
        style.set('font-weight', 'bold');
      } else {
        style.set('font-weight', 'normal');
      }
    }
    return Object.fromEntries(style);
  } catch (err) {
    /* empty */
  }
}

// interface PlainLabelProps {
//   labelId: string;
//   labelText: string;
//   labeltoolTip?: string;
// }

export function AddPlainLabel(labelId: string, text: any) {
  try {
    return (
      <div>
        <StateLabel
          labelId={labelId}
          labelDisplayText={text}
          labelStyle={GetStyle(labelId)}
        />
      </div>
    );
  } catch (err) {
    /* empty */
  }
}

export function AddPlainLabelWithBold(labelId: string, text: any, boldStatus: boolean) {
  try {
    return (
      <div>
        <StateLabel
          labelId={labelId}
          labelDisplayText={text}
          labelStyle={GetBoldStyledObject(labelId, boldStatus)}
        />
      </div>
    );
  } catch (err) {
    /* empty */
  }
}

export function AddSymboLabelWithSuffix(
  labelId: string,
  component_id: any,
  symbolId: any,
  suffix: string
) {
  try {
    return (
      <div>
        <StateLabel
          labelId={labelId}
          labelDisplayText={GetSymbolValue(component_id, symbolId)}
          labelSuffixText={suffix}
          labelStyle={GetStyle(labelId)}
          symbolListeners={[symbolId]}
        />
      </div>
    );
  } catch (err) {
    /* empty */
  }
}

export function AddSymboLabelWithSuffixWithBold(
  labelId: string,
  component_id: any,
  symbolId: any,
  suffix: string,
  boldStatus: boolean
) {
  try {
    return (
      <div>
        <StateLabel
          labelId={labelId}
          labelDisplayText={GetSymbolValue(component_id, symbolId)}
          labelSuffixText={suffix}
          labelStyle={GetBoldStyledObject(labelId, boldStatus)}
          symbolListeners={[symbolId]}
        />
      </div>
    );
  } catch (err) {
    /* empty */
  }
}

export function AddMinMaxSymboLabelWithSuffix(
  labelId: string,
  component_id: string,
  symbolId: any,
  suffix: string,
  minValue: any,
  maxValue: any,
  changeColor: any,
  labelTooltip: any
) {
  function ColorChangeStatus(minValue: unknown, maxValue: unknown, newValue: unknown) {
    const status =
      Number(newValue) >= Number(minValue) && Number(newValue) <= Number(maxValue) ? true : false;
    return !status;
  }
  function customLabelConfigOnSymbolChange(symbolId: unknown, currentSymbolValue: unknown) {
    ChangeCustomLabelComponentState(
      symbolId,
      currentSymbolValue,
      GetColeredStyledObject(
        labelId,
        ColorChangeStatus(minValue, maxValue, currentSymbolValue),
        changeColor
      ),
      true,
      null
    );
  }
  try {
    const symbolValue = GetSymbolValue(component_id, symbolId);
    return (
      <div>
        <StateLabel
          labelId={labelId}
          labelDisplayText={symbolValue}
          labelSuffixText={suffix}
          labelStyle={GetColeredStyledObject(
            labelId,
            ColorChangeStatus(minValue, maxValue, symbolValue),
            changeColor
          )}
          symbolListeners={[symbolId]}
          labelTooltip={labelTooltip}
          customLabelConfigOnSymbolChange={customLabelConfigOnSymbolChange}
        />
      </div>
    );
  } catch (err) {
    /* empty */
  }
}

export function AddPrefixDivSymbolLabel(
  id: string,
  component_id: string,
  symbolId: string,
  InputFormat: (arg0: any) => void
) {
  function customLabelConfigOnSymbolChange(symbolId: any, value: any) {
    ChangeCustomLabelComponentState(symbolId, InputFormat(value), null, null, null);
  }
  try {
    return (
      <div>
        <StateLabel
          labelId={id}
          labelDisplayText={InputFormat(GetSymbolValue(component_id, symbolId))}
          labelStyle={GetStyle(id)}
          symbolListeners={[symbolId]}
          customLabelConfigOnSymbolChange={customLabelConfigOnSymbolChange}
        />
      </div>
    );
  } catch (err) {
    /* empty */
  }
}
