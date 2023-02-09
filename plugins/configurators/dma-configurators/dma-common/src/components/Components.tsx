/*******************************************************************************
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
 *******************************************************************************/
import {
  GetSymbolArray,
  GetSymbolLabelName,
  GetSymbolMaxValue,
  GetSymbolMinValue,
  GetSymbolReadOnlyStatus,
  GetSymbolType,
  GetSymbolValue,
  GetSymbolVisibleStatus,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import { error } from '@mplab_harmony/harmony-plugin-core-service/build/log/CustomConsole';
import React from 'react';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import DropDown from '@mplab_harmony/harmony-plugin-ui/build/components/DropDown';
import InputNumber from '@mplab_harmony/harmony-plugin-ui/build/components/InputNumber';
import { DisplayLabel } from '@mplab_harmony/harmony-plugin-ui/build/components/Label';

export let globalSymbolStyleData = new Map<any, Map<string, string>>();
export let globalSymbolSStateData = new Map<any, any>();
export let defaultInputNumberStyleMap = new Map<string, string>();
export let defaultDropDownStyleMap = new Map<string, string>();

export enum SymbolType {
  DropDown,
  InputNumber,
  CheckBox,
  String,
}

function Component(props: {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  onChange: (arg0: any) => void;
}) {
  let component: any;
  let value = GetSymbolValue(props.componentId, props.symbolId);
  if (value === null) {
    error('Missing_Symbol: ' + props.symbolId);
    return null;
  }

  let symbolVisibleStatus =
    GetSymbolVisibleStatus(props.componentId, props.symbolId) === true
      ? true
      : false;
  if (!symbolVisibleStatus) {
    return null;
  }

  let symbolType = GetComponentType({
    componentId: props.componentId,
    symbolID: props.symbolId,
  });

  switch (symbolType as any) {
    case SymbolType.DropDown:
      component = (
        <DropDown
          componentId={props.componentId}
          symbolId={props.symbolId}
          symbolListeners={props.symbolListeners}
          symbolValue={value}
          symbolArray={GetSymbolArray(props.componentId, props.symbolId)}
          styleObject={GetDropDownStyle(props.symbolId)}
          className={null}
          readOnly={GetSymbolReadOnlyStatus(props.componentId, props.symbolId)}
          visible={symbolVisibleStatus}
          onChange={(target) => props.onChange(target.target)}
        />
      );
      break;
    case SymbolType.InputNumber:
      component = (
        <InputNumber
          componentId={props.componentId}
          symbolId={props.symbolId}
          symbolValue={value}
          symbolListeners={props.symbolListeners}
          minFractionValue={GetMinFractionValueBasedSymbolType(
            props.componentId,
            props.symbolId
          )}
          minValue={GetSymbolMinValue(props.componentId, props.symbolId)}
          maxValue={GetSymbolMaxValue(props.componentId, props.symbolId)}
          styleObject={GetInputNumberStyle(props.symbolId)}
          className={null}
          readOnly={GetSymbolReadOnlyStatus(props.componentId, props.symbolId)}
          onChange={(target) => props.onChange(target.target)}
          visible={symbolVisibleStatus}
        />
      );
      break;
    case SymbolType.CheckBox:
      component = (
        <CheckBox
          componentId={props.componentId}
          symbolId={props.symbolId}
          symbolListeners={props.symbolListeners}
          symbolValue={value}
          styleObject={GetStyle(props.symbolId)}
          className={null}
          readOnly={GetSymbolReadOnlyStatus(props.componentId, props.symbolId)}
          visible={symbolVisibleStatus}
          onChange={(target) => props.onChange(target.target)}
        />
      );
      break;
    case SymbolType.String:
      component = (
        <div className="p-text-italic">
          <DisplayLabel labelName={value} />
        </div>
      );
      break;
    default:
      error('Invalid SymbolType.');
  }
  return component;
}

function ComponentWithLabel(props: {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  onChange: (arg0: any) => void;
}) {
  let component = Component(props);
  if (component === null) {
    return null;
  }
  return (
    <div className="grid">
      <div className="col">
        <DisplayLabel
          labelName={GetSymbolLabelName(props.componentId, props.symbolId)}
        />{' '}
      </div>
      <div className="col-fixed" style={{ width: 510 }}>
        {component}
      </div>
    </div>
  );
}

function ComponentWithOutLabel(props: {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  onChange: (arg0: any) => void;
}) {
  return (
    <div>
      <Component
        componentId={props.componentId}
        symbolId={props.symbolId}
        symbolListeners={props.symbolListeners}
        onChange={props.onChange}
      />
    </div>
  );
}

export function GetMinFractionValueBasedSymbolType(
  componentId: any,
  symbolID: any
) {
  let typeofSymbol = GetSymbolType(componentId, symbolID);
  if (typeofSymbol === 'Float') {
    return 1;
  }
  return 0;
}

function GetComponentType(props: { componentId: any; symbolID: any }) {
  let typeofSymbol = GetSymbolType(props.componentId, props.symbolID);
  let type: any;
  switch (typeofSymbol) {
    case 'Boolean':
      type = SymbolType.CheckBox;
      break;
    case 'Integer':
    case 'Long':
    case 'Hex':
    case 'Float':
      type = SymbolType.InputNumber;
      break;
    case 'KeyValueSet':
    case 'ComboSymbol':
    case 'Combo':
      type = SymbolType.DropDown;
      break;
    case 'String':
      type = SymbolType.String;
      break;
    default:
      error('Invalid SymbolType ' + props.symbolID);
  }
  return type;
}

export function GetUIComponentWithLabel(props: {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  onChange: (arg0: any) => void;
}) {
  return (
    <div>
      <ComponentWithLabel
        componentId={props.componentId}
        symbolId={props.symbolId}
        symbolListeners={props.symbolListeners}
        onChange={props.onChange}
      />
    </div>
  );
}

export function GetUIComponentWithOutLabel(props: {
  componentId: any;
  symbolId: any;
  symbolListeners: any;
  onChange: (arg0: any) => void;
}) {
  return (
    <div>
      <ComponentWithOutLabel
        componentId={props.componentId}
        symbolId={props.symbolId}
        symbolListeners={props.symbolListeners}
        onChange={props.onChange}
      />
    </div>
  );
}

export function GetStyle(symbolId: string) {
  let style = globalSymbolStyleData.get(symbolId);
  if (style !== undefined) {
    return Object.fromEntries(style);
  }
}

function GetInputNumberStyle(symbolId: string) {
  let style = globalSymbolStyleData.get(symbolId);
  if (style !== undefined) {
    return Object.fromEntries(style);
  } else {
    return Object.fromEntries(defaultInputNumberStyleMap);
  }
}

function GetDropDownStyle(symbolId: string) {
  let style = globalSymbolStyleData.get(symbolId);
  if (style !== undefined) {
    return Object.fromEntries(style);
  } else {
    return Object.fromEntries(defaultDropDownStyleMap);
  }
}

let requiredStyles = ['position', 'top', 'left', 'width', 'height'];

export function StoreSymbolStyle(
  toolBarHeight: string,
  symbolId: string,
  styleMap: Map<any, any>
) {
  let map = new Map<string, string>();
  styleMap.forEach((value, key) => {
    if (key === symbolId) {
      for (let k in value) {
        // if (requiredStyles.includes(k)) {
        if (k === 'top' || k === 'left') {
          let v = value[k];
          v = v.replace('px', '');
          v = Number(v) + 10;
          if (k === 'top') {
            v = Number(v) + Number(toolBarHeight.replace('px', ''));
          }
          map.set(k, v + 'px');
        } else if (k === 'width' || k === 'height') {
          let v = value[k];
          map.set(k, v);
        } else {
          map.set(k, value[k]);
        }
      }
      // }
    }
  });
  globalSymbolStyleData.set(symbolId, map);
}

export default class Components {}
