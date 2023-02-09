import Header from './ToolBar';
import React from 'react';

import { SetComponentId } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import MPURegionSettings from '../components/MPURegionSettings';

import { ChangeValueState } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';

import { GetSymbolValue } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import MPUGlobalSettings from '../components/MPUGlobalSettings';
import MPUContextProvider from '../../store/MPUContextProvider';

export let progressStatus = true;

export let component_id = 'core';
export let toolBarHeight = '60px';

const MainBlock = () => {
  SetComponentId(component_id);

  const getMPURegions = () => {
    const count = GetSymbolValue(component_id, 'MPU_NUMBER_REGIONS');
    const arr = [];
    for (let i = 0; i < count; i++) {
      arr.push(i);
    }
    return arr;
  };

  const MPURegions = getMPURegions();

  (window as any).SymbolValueChanged = (value: any) => {
    if (value !== null && value !== undefined) {
      const symbolData = value.split('M*C');
      const symbolId: string = symbolData[0];
      const symbolValue = symbolData[1];
      // const readOnlyStatus = convertToBoolean(symbolData[2]);
      // const visibleStatus = true;

      if (globalSymbolSStateData.get(symbolId) != null) {
        ChangeValueState(symbolId, symbolValue);
        // ChangeComponentState(
        //   symbolId,
        //   symbolValue,
        //   readOnlyStatus,
        //   visibleStatus
        // );
      }
    }
  };

  return (
    <MPUContextProvider>
      <Header />
      <MPUGlobalSettings regions={MPURegions} />
      <MPURegionSettings regions={MPURegions} />
    </MPUContextProvider>
  );
};

export default MainBlock;
