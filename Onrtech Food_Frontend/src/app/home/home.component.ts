import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  @ViewChild('dashboardIframe') dashboardIframe!: ElementRef<HTMLIFrameElement>;
  
  publicDashboardUrl: SafeResourceUrl | null = null;
  isLoading = true;

  constructor(private sanitizer: DomSanitizer) {}

  ngOnInit(): void {
    this.loadPublicDashboard();
  }

  loadPublicDashboard(): void {
    // Public dashboard showing only Product Sheet for non-authenticated users
    const powerBiUrl = 'https://app.fabric.microsoft.com/reportEmbed?reportId=733105bc-4238-4881-b277-b2571edabe79&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730&navContentPaneEnabled=false&filterPaneEnabled=false&toolbarPaneEnabled=false';
    
    this.publicDashboardUrl = this.sanitizer.bypassSecurityTrustResourceUrl(powerBiUrl);
  }

  onIframeLoad(): void {
    this.isLoading = false;
  }

  toggleFullscreen(): void {
    const wrapper = document.getElementById('dashboardWrapper');
    
    if (!wrapper) {
      console.error('Dashboard wrapper not found');
      return;
    }

    if (!document.fullscreenElement) {
      // Enter fullscreen
      if (wrapper.requestFullscreen) {
        wrapper.requestFullscreen();
      } else if ((wrapper as any).webkitRequestFullscreen) {
        (wrapper as any).webkitRequestFullscreen();
      } else if ((wrapper as any).mozRequestFullScreen) {
        (wrapper as any).mozRequestFullScreen();
      } else if ((wrapper as any).msRequestFullscreen) {
        (wrapper as any).msRequestFullscreen();
      }
    } else {
      // Exit fullscreen
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if ((document as any).webkitExitFullscreen) {
        (document as any).webkitExitFullscreen();
      } else if ((document as any).mozCancelFullScreen) {
        (document as any).mozCancelFullScreen();
      } else if ((document as any).msExitFullscreen) {
        (document as any).msExitFullscreen();
      }
    }
  }
}
