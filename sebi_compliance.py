class SEBIChecker:
    def check_compliance(self, company_data):
        """Basic SEBI compliance checks"""
        warnings = []
        
        # Check promoter pledge
        if company_data.get('promoter_pledge', 0) > 30:
            warnings.append(f"High promoter pledge ({company_data['promoter_pledge']}%) - may indicate financial stress")
            
        # Check auditor remarks
        if 'qualified' in company_data.get('auditor_report', '').lower():
            warnings.append("Auditor report contains qualifications - examine carefully")
            
        # Check related party transactions
        if company_data.get('related_party_transactions', 0) > 10:
            warnings.append(f"High related party transactions ({company_data['related_party_transactions']}% of revenue) - potential governance issue")
            
        return warnings if warnings else ["No major SEBI compliance issues detected"]