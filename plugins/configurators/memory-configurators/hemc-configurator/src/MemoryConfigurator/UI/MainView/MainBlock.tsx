import Header from './ToolBar';
import React from 'react';
import { SetComponentId } from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';

import { globalSymbolSStateData } from '@mplab_harmony/harmony-plugin-ui/build/components/Components';
import HEMCConfigurations from './HEMCConfgurations';

import { ChangeValueState } from '@mplab_harmony/harmony-plugin-ui/build/utils/ComponentStateChangeUtils';

export let progressStatus = true;

export let component_id = 'hemc';
export let toolBarHeight = '60px';

const MainBlock = () => {
  SetComponentId(component_id);

  (window as any).SymbolValueChanged = (value: any) => {
    if (value !== null && value !== undefined) {
      const symbolData = value.split('M*C');
      const symbolId: string = symbolData[0];
      const symbolValue = symbolData[1];

      if (globalSymbolSStateData.get(symbolId) != null) {
        ChangeValueState(symbolId, symbolValue);
      }
    }
  };

  return (
    <React.Fragment>
      <Header />
      <HEMCConfigurations />
    </React.Fragment>
  );
};

export default MainBlock;
