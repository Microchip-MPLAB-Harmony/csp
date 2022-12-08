import {
  GetSymbolValue,
  clearSymbol,
} from '@mplab_harmony/harmony-plugin-core-service/build/database-access/SymbolAccess';
import CheckBox from '@mplab_harmony/harmony-plugin-ui/build/components/CheckBox';
import { useContext } from 'react';
import { component_id } from '../MainView/MainBlock';
import style from './MPUGlobalSettings.module.css';
import MPUContext from '../../store/MPUContext';
import RecommendedSettingsComp from './RecommendedSettingsComp';

interface MPUProps {
  regions: number[];
}

const MPUGlobalSettings = (props: MPUProps) => {
  const MPUctx = useContext(MPUContext);

  const clearUserValuesFromRegions = (value: boolean) => {
    if (value === true) {
      for (let i in props.regions) {
        clearSymbol(component_id, 'MPU_Region_' + i + '_Enable');
        clearSymbol(component_id, 'MPU_Region_Name' + i);
        clearSymbol(component_id, 'MPU_Region_' + i + '_Address');
        clearSymbol(component_id, 'MPU_Region_' + i + '_Size');
        clearSymbol(component_id, 'MPU_Region_' + i + '_Type');
        clearSymbol(component_id, 'MPU_Region_' + i + '_Access');
        clearSymbol(component_id, 'MPU_Region_' + i + '_Execute');
        clearSymbol(component_id, 'MPU_Region_' + i + '_Share');
      }
    }
  };

  return (
    <div className={style['grid-container']}>
      <CheckBox
        componentId={component_id}
        symbolId={'CoreUseMPU'}
        symbolListeners={['CoreUseMPU']}
        symbolValue={GetSymbolValue(component_id, 'CoreUseMPU')}
        styleObject={{}}
        className={{}}
        readOnly={false}
        visible={true}
        onChange={(checked) => {
          MPUctx.updatePUEnabled(checked);
        }}
      />
      <div>Enable MPU</div>

      <CheckBox
        componentId={component_id}
        symbolId={'CoreMPU_HFNMIENA'}
        symbolListeners={['CoreMPU_HFNMIENA']}
        symbolValue={GetSymbolValue(component_id, 'CoreMPU_HFNMIENA')}
        styleObject={{}}
        className={{}}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
      <div>HFNMIENA (Enable MPU during HARDFAULT, NMI or FAULTMASK is set)</div>

      <CheckBox
        componentId={component_id}
        symbolId={'CoreMPU_PRIVDEFENA'}
        symbolListeners={['CoreMPU_PRIVDEFENA']}
        symbolValue={GetSymbolValue(component_id, 'CoreMPU_PRIVDEFENA')}
        styleObject={{}}
        className={{}}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
      />
      <div>
        PRIVDEFENA (Enable priviledged software access to the default memory
        map)
      </div>

      <RecommendedSettingsComp
        componentId={component_id}
        symbolId={'CoreMPU_DEFAULT'}
        symbolListeners={['CoreMPU_DEFAULT']}
        symbolValue={GetSymbolValue(component_id, 'CoreMPU_DEFAULT')}
        styleObject={{}}
        className={{}}
        readOnly={!MPUctx.MPUEnabled}
        visible={true}
        onChange={() => {}}
        beforeChange={clearUserValuesFromRegions}
      />
      <div>Use Recommended Settings</div>
    </div>
  );
};

export default MPUGlobalSettings;
