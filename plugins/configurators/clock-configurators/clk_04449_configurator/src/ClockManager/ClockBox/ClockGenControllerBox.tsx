import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import { useContext, useState } from 'react';
import {
    configSymbolApi,
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
import { ControlInputNoInterface, GetButton, getDynamicInputNoSymbolsFromJSON, LoadDynamicInputNoComponents } from '../ClockHelper/LoadDynamicInputNoComponents';
import { Dialog } from 'primereact/dialog';
import ClockGenAutoCalc from './ClockGenAutoCalc';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';


const ClockGenControllerBox = (props: {
    ClkGenControllerData: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => {
    const { componentId = 'core' } = useContext(PluginConfigContext);

    const [dynamicSymbolInfo] = useState(() =>
        getDynamicSymbolsFromJSON(props.ClkGenControllerData)
    );

    const [dynamicInputNoSymbolsInfo] = useState(() => {
        let inputNoFields: ControlInputNoInterface[] = getDynamicInputNoSymbolsFromJSON(props.ClkGenControllerData);
        inputNoFields.forEach((e) => {
            configSymbolApi.getSymbol(componentId, e.symbol_id ?? "").then((data) => e.tooltip = `Min: ${data.min}, Max: ${data.max}`)
        })
        return inputNoFields;
    });

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
    const clockGenDivMaxFreq = Math.min(clockSourceFreq.value / 2, clkGenMaxFreq)
    const clkGenName = "System Clock/Clock Generator 1";
    const maxFreqLabel = " (Max Frequency = " + GetClockDisplayFreqValue(clkGenMaxFreq) + ")";
    const textColorClkGenOutFreq = Number(clkGenOutfreq.value) > clkGenMaxFreq ? 'red' : 'black';

    return (
        <div>
            <label
                className={props.cx('clkGenLabel')}
            >
                <span style={{ fontWeight: 'bold' }}>{clkGenName} </span>
                <span style={{ fontWeight: 'bold', color: textColorClkGenOutFreq }}>{maxFreqLabel} </span>
            </label>
            <LoadDynamicComponents
                componentId={componentId}
                dynamicSymbolsInfo={dynamicSymbolInfo}
                cx={props.cx}
            />
            <LoadDynamicInputNoComponents
                componentId={componentId}
                dynamicSymbolsInfo={dynamicInputNoSymbolsInfo}
                cx={props.cx}
                disable={!isClkGenDivEnabled.value}
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
                dialogHeight='18rem'
            />
            <ResetSymbolsIcon
                tooltip={'Reset Clock Generator ' + '1' + ' Settings to default value'}
                className={props.cx('clkGen' + '1' + '_Reset')}
                componentId={componentId}
                resetSymbolsArray={clkGenResetSymbols}
            />
            <label
                className={props.cx('ClkGenSysFreq')}
            >
                <span style={{ fontWeight: 'bold', color: textColorClkGenOutFreq }}>{GetClockDisplayFreqValue(clkGenOutfreq.value)} </span>
                {/* <span style={{ color: 'blue' }}>{'<= ' + GetClockDisplayFreqValue(maxClkGenOut)} </span> */}
            </label>
            {isClkGenDivEnabled.value &&
                <GetButton
                    buttonDisplayText={'Auto Calculate...'}
                    className={props.cx('ClkGenAutoCalcButton')}
                    toolTip={'click here for Clock Generator Auto Calculation'}
                    buttonClick={clkGenAutoCalculationButtonClicked}
                    disabled={false}
                />}
            <Dialog
                header='Auto Calculate System Clock frequency'
                visible={dialogStatus}
                maximizable={true}
                style={{ width: '55rem', height: '30rem' }}
                onHide={() => {
                    dialogClosed(false);
                }}>
                <ClockGenAutoCalc
                    index={"1"}
                    componentId={componentId}
                    inputClkSrcFreq={clockSourceFreq.value}
                    reqClkSrcFreq={clkGenOutfreq.value}
                    maxClkGenFreq={clockGenDivMaxFreq}
                    close={() => {
                        dialogClosed(false);
                    }}
                />
            </Dialog>
        </div>
    );
};

export default ClockGenControllerBox;