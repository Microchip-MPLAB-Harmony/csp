import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
    KeyValueSetRadio,
    PluginConfigContext,
    useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
    getDynamicLabelsFromJSON,
    getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';


const ClockGenControllerBox = (props: {
    ClkGenControllerData: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => {
    const { componentId = 'core' } = useContext(PluginConfigContext);

    const [dynamicSymbolInfo] = useState(() =>
        getDynamicSymbolsFromJSON(props.ClkGenControllerData)
    );

     const [dynamicLabelSymbolsInfo] = useState(() => getDynamicLabelsFromJSON(props.ClkGenControllerData));

    const clockSource = useKeyValueSetSymbol({
        componentId,
        symbolId: 'clkGen1CON__NOSC'
    });

    let clkGenSymbols = [
        'clkGen' +'1' + 'enableFailSafeClock',
        'clkGen' +'1' + 'CON__BOSC'
    ];

    let clkGenResetSymbols = [
        'clkGen' +'1' + 'CON__NOSC',
        'clkGen' +'1' + 'IsDividerEnabled',
        'clkGen' +'1' + 'DIV__INTDIV',
        'clkGen' +'1' + 'DIV__FRACDIV',
        'clkGen' +'1' + 'enableFailSafeClock',
        'clkGen' +'1' + 'CON__BOSC'
    ];

    return (
        <div>
            <LoadDynamicComponents
                componentId={componentId}
                dynamicSymbolsInfo={dynamicSymbolInfo}
                cx={props.cx}
            />
            <LoadDynamicFreqencyLabels
                componentId={componentId}
                dynamicLabelSymbolsInfo={dynamicLabelSymbolsInfo}
                cx={props.cx}
            />
            <PlainLabel
                disPlayText={'Use Clock Divider'}
                className={props.cx('ClkGenDivEn')}
            />
            <KeyValueSetRadio
                keyValueSetSymbolHook={clockSource}
                classPrefix='ClkGenRadio'
                labelClassPrefix='ClkGenRadioName'
                classResolver={props.cx}></KeyValueSetRadio>
            <SettingsDialog
                tooltip={'Clock Generator ' + '1' + ' Advanced Settings'}
                componentId={componentId}
                className={props.cx('clkGen' + '1' + '_Settings')}
                symbolArray={clkGenSymbols}
                dialogWidth='50rem'
                dialogHeight='40rem'
            />
            <ResetSymbolsIcon
                tooltip={'Reset Clock Generator ' + '1'  + ' Settings to default value'}
                className={props.cx('clkGen' + '1' + '_Reset')}
                componentId={componentId}
                resetSymbolsArray={clkGenResetSymbols}
            />

        </div>
    );
};

export default ClockGenControllerBox;