import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
    PluginConfigContext
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
    getDynamicLabelsFromJSON,
} from 'clock-common/lib/Tools/ClockJSONTools';

import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';

const ClockGen2and3ControllerBox = (props: {
    ClkGen2and3ControllerData: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => {
    const { componentId = 'core' } = useContext(PluginConfigContext);


     const [dynamicLabelSymbolsInfo] = useState(() => getDynamicLabelsFromJSON(props.ClkGen2and3ControllerData));

    let clkGen2Symbols = [
        'clkGen' +'2' + 'enableFailSafeClock',
        'clkGen' +'2' + 'CON__BOSC'
    ];

    let clkGen3Symbols = [
        'clkGen' +'3' + 'enableFailSafeClock',
        'clkGen' +'3' + 'CON__BOSC'
    ];

    return (
        <div>
            <LoadDynamicFreqencyLabels
                componentId={componentId}
                dynamicLabelSymbolsInfo={dynamicLabelSymbolsInfo}
                cx={props.cx}
            />
            <SettingsDialog
                tooltip={'Clock Generator ' + '2' + ' Advanced Settings'}
                componentId={componentId}
                className={props.cx('clkGen' + '2' + '_Settings')}
                symbolArray={clkGen2Symbols}
                dialogWidth='40rem'
                dialogHeight='20rem'
            />
            <ResetSymbolsIcon
                tooltip={'Reset Clock Generator ' + '2'  + ' Settings to default value'}
                className={props.cx('clkGen' + '2' + '_Reset')}
                componentId={componentId}
                resetSymbolsArray={clkGen2Symbols}
            />
            <SettingsDialog
                tooltip={'Clock Generator ' + '3' + ' Advanced Settings'}
                componentId={componentId}
                className={props.cx('clkGen' + '3' + '_Settings')}
                symbolArray={clkGen3Symbols}
                dialogWidth='40rem'
                dialogHeight='20rem'
            />
            <ResetSymbolsIcon
                tooltip={'Reset Clock Generator ' + '3'  + ' Settings to default value'}
                className={props.cx('clkGen' + '3' + '_Reset')}
                componentId={componentId}
                resetSymbolsArray={clkGen3Symbols}
            />
            <PlainLabel
                className = {props.cx('clkGen2ClkSrc')}
                disPlayText='FRC'
            />
            <PlainLabel
                className = {props.cx('clkGen3ClkSrc')}
                disPlayText='BFRC'
            />
        </div>
    );
};

export default ClockGen2and3ControllerBox;