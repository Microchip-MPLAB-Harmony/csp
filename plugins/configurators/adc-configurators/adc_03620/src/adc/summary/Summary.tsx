import { Accordion, AccordionTab } from "primereact/accordion";
import CommonADCSummary from "./CommonADCSummary";
import { useSummaryData } from "./useSummaryData";
import ADCModuleSummary from "./ADCModuleSummary";

export type SummaryDataProps = {
  accordionHeader: string;
  summaryDetails: FieldsetDetails[] | Symbols[];
};
export type FieldsetDetails = {
  fieldSetHeader: string;
  symbols: Symbols[];
};
export type Symbols = {
  label: string;
  value: string | number | boolean;
};

const Summary = () => {
  const { summaryData } = useSummaryData();
  const AccordTab = (summary: SummaryDataProps) => {
    if (summary.accordionHeader === "General ADC Config") {
      return (
        <CommonADCSummary
          fieldsetDetails={summary.summaryDetails as FieldsetDetails[]}
        />
      );
    } else
      return <ADCModuleSummary accordionHeader={summary.accordionHeader} />;
  };
  return (
    <div>
      <Accordion activeIndex={0} style={{ width: "80vw" }}>
        {summaryData.map((summary: SummaryDataProps) => {
          return (
            <AccordionTab
              key={summary.accordionHeader}
              header={summary.accordionHeader}
            >
              {AccordTab(summary)}
            </AccordionTab>
          );
        })}
      </Accordion>
    </div>
  );
};
export default Summary;
