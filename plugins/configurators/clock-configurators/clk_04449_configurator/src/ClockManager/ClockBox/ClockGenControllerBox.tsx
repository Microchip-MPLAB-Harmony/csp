import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
    KeyValueSetRadio,
    PluginConfigContext,
    useBooleanSymbol,
    useIntegerSymbol,
    useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import {
    getDynamicLabelsFromJSON,
    getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { GetButton } from '../ClockHelper/LoadDynamicInputNoComponents';
import { Dialog } from 'primereact/dialog';
import ClockGenAutoCalc from './ClockGenAutoCalc';


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

    const clockSourceFreq = useIntegerSymbol({
        componentId,
        symbolId: 'clkGen' + '1' + 'ClkSrcFrequency'
    });

    const clkGenOutfreq = useIntegerSymbol({
        componentId,
        symbolId: 'clkGen' + '1' + 'OutFrequency'
    });

    const isClkGenDivEnabled = useBooleanSymbol({
        componentId,
        symbolId: 'clkGen' + '1' + 'IsDividerEnabled'
    });

    let clkGenSymbols = [
        'clkGen' + '1' + 'enableFailSafeClock',
        'clkGen' + '1' + 'CON__BOSC'
    ];

    let clkGenResetSymbols = [
        'clkGen' + '1' + 'CON__NOSC',
        'clkGen' + '1' + 'IsDividerEnabled',
        'clkGen' + '1' + 'DIV__INTDIV',
        'clkGen' + '1' + 'DIV__FRACDIV',
        'clkGen' + '1' + 'enableFailSafeClock',
        'clkGen' + '1' + 'CON__BOSC'
    ];

    const [dialogStatus, setdialogStatus] = useState(false);

    function clkGenAutoCalculationButtonClicked() {
        setdialogStatus(true);
    }

    const dialogClosed = (acceptStatus: boolean) => {
        setdialogStatus(false);
    };

    const clkGenMaxFreq = 200000000
    const clockGenDivMaxFreq = Math.min(clockSourceFreq.value/2,clkGenMaxFreq)
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
                tooltip={'Reset Clock Generator ' + '1' + ' Settings to default value'}
                className={props.cx('clkGen' + '1' + '_Reset')}
                componentId={componentId}
                resetSymbolsArray={clkGenResetSymbols}
            />
            {isClkGenDivEnabled.value &&
            <GetButton
                buttonDisplayText={'Auto Calculate...'}
                className={props.cx('ClkGenAutoCalcButton')}
                toolTip={'click here for Clock Generator Auto Calculation'}
                buttonClick={clkGenAutoCalculationButtonClicked}
                disabled = {false}
            />}
           <Dialog
                header='Auto Calculate System Clock frequency'
                visible={dialogStatus}
                maximizable={true}
                style={{ width: '55rem', height: '45rem' }}
                onHide={() => {
                    dialogClosed(false);
                }}>
                <ClockGenAutoCalc
                    index={"1"}
                    componentId={componentId}
                    inputClkSrcFreq={clockSourceFreq.value}
                    reqClkSrcFreq = {clkGenOutfreq.value}
                    maxClkGenFreq={clockGenDivMaxFreq}
                    close = {() => {
                        dialogClosed(false);
                    }}
                />
            </Dialog>
        </div>
    );
};

export default ClockGenControllerBox;